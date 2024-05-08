from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from server.models import Book
from server.models import Author
from server.models import Shelf
from server.models import Publisher
from server.models import BookState
from server.models import User
from server.models import LoanToken

from server.serializer import BookSerializer, LoanTokenSerializer
from server.serializer import AuthorSerializer
from server.serializer import ShelfSerializer
from server.serializer import BookStateSerializer
from server.serializer import PublisherSerializer
from server.serializer import UserSerializer

from server.serializer import AuthorSerializerList
from server.serializer import BookSerializerList
from server.serializer import ShelfSerializerList
from server.serializer import BookStateSerializerList
from server.serializer import PublisherSerializerList
from server.serializer import UserSerializerList



class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_queryset(self):
        return Author.objects.filter(active=True)

    def get_serializer_class(self):
        if self.action == "list":
            return AuthorSerializerList
        return AuthorSerializer


class ShelfViewSet(ModelViewSet):

    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer

    def get_queryset(self):
        return Shelf.objects.filter(active=True)

    def get_serializer_class(self):

        if self.action == "list":
            return ShelfSerializerList

        return ShelfSerializer


class BookStateViewSet(ModelViewSet):

    queryset = BookState.objects.all()
    serializer_class = BookStateSerializer

    def get_queryset(self):
        return BookState.objects.filter(active=True)

    def get_serializer_class(self):

        if self.action == "list":
            return BookStateSerializerList

        return BookStateSerializer


class BookViewSet(ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter(active=True)

    def get_serializer_class(self):

        if self.action == "list":
            return BookSerializerList

        return BookSerializer
    
    @action(detail=True, methods=['POST'])
    def loan(self, request: Request, pk=None):
        book = Book.objects.get(pk=pk)
        token = request.data.get('token')
        if token is None:
            return Response({'error': 'Token is required.'}, status=status.HTTP_400_BAD_REQUEST)
        if book.loan(token):
            return Response({'message': 'Book loaned successfully.'}, status=status.HTTP_200_OK)
        return Response({'error': 'Book loan failed.'}, status=status.HTTP_400_BAD_REQUEST)


class PublisherViewSet(ModelViewSet):

    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

    def get_queryset(self):
        return Publisher.objects.filter(active=True)

    def get_serializer_class(self):

        if self.action == "list":
            return PublisherSerializerList

        return PublisherSerializer


class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    mail_parameter = openapi.Parameter('mail', openapi.IN_QUERY, description="The mail of the user", type=openapi.TYPE_STRING)
    password_parameter = openapi.Parameter('password', openapi.IN_QUERY, description="The password of the user", type=openapi.TYPE_STRING)

    def get_queryset(self):
        return User.objects.filter(active=True)

    def get_serializer_class(self):

        if self.action == "list":
            return UserSerializerList

        return UserSerializer
    
    @swagger_auto_schema(
        method='post', 
        operation_description="Get a loan token with user mail and SHA-256 password",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['mail', 'password'],
            properties={
                'mail': {
                    'type': openapi.TYPE_STRING,
                    'description': 'User email address',
                },
                'password': {
                    'type': openapi.TYPE_STRING,
                    'description': 'SHA-256 hashed password',
                },
            }
        ),
        responses={200: LoanTokenSerializer()}
    )
    @action(detail=False, methods=['POST'])
    def get_loan_token(self, request: Request):
        """
        Get a loan token with user email and SHA-256 password.

        Parameters:
        - mail (str): User email address.
        - password (str): SHA-256 hashed password.

        Returns:
        - 200: LoanTokenSerializer - Token created.
        """
        email = request.data.get('mail')
        password = request.data.get('password')
        
        if email is None or password is None:
            return Response({'error': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        token = LoanToken.create_token(mail=email, password=password)
        if token:
            return Response(LoanTokenSerializer(token).data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)