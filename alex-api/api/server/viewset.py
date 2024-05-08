from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request

from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Parameter
from drf_yasg.openapi import IN_QUERY
from drf_yasg.openapi import TYPE_STRING

from server.models import Book
from server.models import Author
from server.models import Shelf
from server.models import Publisher
from server.models import BookState
from server.models import User
from server.models import LoanToken

from server.serializer import BookSerializer
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
    mail_parameter = Parameter('mail', IN_QUERY, description="The mail of the user", type=TYPE_STRING)
    password_parameter = Parameter('password', IN_QUERY, description="The password of the user", type=TYPE_STRING)

    def get_queryset(self):
        return User.objects.filter(active=True)

    def get_serializer_class(self):

        if self.action == "list":
            return UserSerializerList

        return UserSerializer
    
    @swagger_auto_schema(method='post', 
                        operation_description="Get a loan token with user mail and sha-256 password",
                        manual_parameters=[mail_parameter, password_parameter], 
                        responses={200: 'Token created'}, 
                        request_body=None)
    @action(detail=False, methods=['POST'])
    def get_loan_token(self, request: Request):
   
        return Response(data = {
            "token" : LoanToken.create_token(
                request.data['mail'],  
                request.data['password']
            )}
        )    
        