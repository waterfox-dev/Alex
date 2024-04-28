from rest_framework.viewsets import ModelViewSet

from server.models import Book
from server.models import Author
from server.models import Shelf
from server.models import Edition
from server.models import BookState
from server.models import BookAvailability

from server.serializer import BookSerializer
from server.serializer import AuthorSerializer
from server.serializer import ShelfSerializer
from server.serializer import EditionSerializer
from server.serializer import BookStateSerializer
from server.serializer import BookAvailabilitySerializer

from server.serializer import AuthorSerializerList
from server.serializer import BookSerializerList
from server.serializer import EditionSerializerList
from server.serializer import ShelfSerializerList
from server.serializer import BookStateSerializerList
from server.serializer import BookAvailabilitySerializerList


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    def get_queryset(self):
        return Author.objects.filter(active=True)
    
    def get_serializer_class(self):
        
        if self.action == 'list':
            return AuthorSerializerList
        
        return AuthorSerializer
    
    
class ShelfViewSet(ModelViewSet):
    
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer
    
    def get_queryset(self):
        return Shelf.objects.filter(active=True)
    
    def get_serializer_class(self):
        
        if self.action == 'list':
            return ShelfSerializerList
        
        return ShelfSerializer    

class EditionViewSet(ModelViewSet):
    
    queryset = Edition.objects.all()
    serializer_class = EditionSerializer
    
    def get_queryset(self):
        return Edition.objects.filter(active=True)
    
    def get_serializer_class(self):
        
        if self.action == 'list':
            return EditionSerializerList
        
        return EditionSerializer
    
class BookStateViewSet(ModelViewSet):
    
    queryset = BookState.objects.all()
    serializer_class = BookStateSerializer
    
    def get_queryset(self):
        return BookState.objects.filter(active=True)

    def get_serializer_class(self):
        
        if self.action == 'list':
            return BookStateSerializerList
        
        return BookStateSerializer

class BookAvailabilityViewSet(ModelViewSet):
    
    queryset = BookAvailability.objects.all()
    serializer_class = BookAvailabilitySerializer
    
    def get_queryset(self):
        return BookAvailability.objects.filter(active=True)
    
    def get_serializer_class(self):
        
        if self.action == 'list':
            return BookAvailabilitySerializerList
        
        return BookAvailabilitySerializer

class BookViewSet(ModelViewSet):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get_queryset(self):
        return Book.objects.filter(active=True)
    
    def get_serializer_class(self):
        
        if self.action == 'list':
            return BookSerializerList
        
        return BookSerializer

class EditionViewSet(ModelViewSet):
    
    queryset = Edition.objects.all()
    serializer_class = EditionSerializer
    
    def get_queryset(self):
        return Edition.objects.filter(active=True)
    
    def get_serializer_class(self):
        
        if self.action == 'list':
            return EditionSerializerList
        
        return EditionSerializer
    