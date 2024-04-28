from rest_framework.serializers import ModelSerializer

from server.models import Book
from server.models import Author
from server.models import Shelf
from server.models import Edition
from server.models import BookState
from server.models import BookAvailability


class AuthorSerializer(ModelSerializer):
        
    class Meta:
        model = Author
        fields = '__all__'


class ShelfSerializer(ModelSerializer):
    
    class Meta:
        model = Shelf
        fields = '__all__'
        

class EditionSerializer(ModelSerializer):
    
    class Meta:
        model = Edition
        fields = '__all__'
        

class BookStateSerializer(ModelSerializer):
    
    class Meta:
        model = BookState
        fields = '__all__'
        

class BookAvailabilitySerializer(ModelSerializer):
    
    class Meta:
        model = BookAvailability
        fields = '__all__'


class BookSerializer(ModelSerializer):
    
    authors = AuthorSerializer(many=True)
    shelf = ShelfSerializer()
    editions = EditionSerializer(many=True)
    state = BookStateSerializer()
    availability = BookAvailabilitySerializer()
    
    
    class Meta:
        model = Book
        fields = ['id', 'isbn', 'title', 'authors', 'shelf', 'editions', 'state', 'availability']
 

class AuthorSerializerList(ModelSerializer):
    
    class Meta:
        model = Author
        fields = ['id', 'name']
        

class ShelfSerializerList(ModelSerializer):
    
    class Meta:
        model = Shelf
        fields = ['id', 'name']
        

class EditionSerializerList(ModelSerializer):
    
    class Meta:
        model = Edition
        fields = ['id', 'name', 'publisher', 'publication_date', 'cover']
        

class BookStateSerializerList(ModelSerializer):
    
    class Meta:
        model = BookState
        fields = ['id', 'name'] 
        

class BookAvailabilitySerializerList(ModelSerializer):
    
    class Meta:
        model = BookAvailability
        fields = ['id', 'name']
        

class BookSerializerList(ModelSerializer):
    
    authors = AuthorSerializerList(many=True)
    shelf = ShelfSerializerList()
    editions = EditionSerializerList(many=True)
    state = BookStateSerializerList()
    availability = BookAvailabilitySerializerList()
    
    
    class Meta:
        model = Book
        fields = ['id', 'isbn', 'title', 'authors', 'shelf', 'editions', 'state', 'availability']