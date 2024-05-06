from rest_framework.serializers import ModelSerializer

from server.models import Book
from server.models import Author
from server.models import Shelf
from server.models import Publisher
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
        

class BookStateSerializer(ModelSerializer):
    
    class Meta:
        model = BookState
        fields = '__all__'
        

class BookAvailabilitySerializer(ModelSerializer):
    
    class Meta:
        model = BookAvailability
        fields = '__all__'

class PublisherSerializer(ModelSerializer):
    
    class Meta:
        model = Publisher
        fields = '__all__'


class BookSerializer(ModelSerializer):
    
    authors = AuthorSerializer(many=True)
    shelf = ShelfSerializer()
    state = BookStateSerializer()
    availability = BookAvailabilitySerializer()
    publisher = PublisherSerializer()
    
    
    class Meta:
        model = Book
        fields = ['id', 'isbn', 'title', 'authors', 'shelf', 'editions', 'state', 'availability', 'publisher', 'cover']
 

class AuthorSerializerList(ModelSerializer):
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'first_name']
        

class ShelfSerializerList(ModelSerializer):
    
    class Meta:
        model = Shelf
        fields = ['id', 'name']
        


class BookStateSerializerList(ModelSerializer):
    
    class Meta:
        model = BookState
        fields = ['id', 'name'] 
        

        

class PublisherSerializerList(ModelSerializer):
    
    class Meta:
        model = Publisher
        fields = ['id', 'name']
        
        
class BookAvailabilitySerializerList(ModelSerializer):
    
    class Meta:
        model = BookAvailability
        fields = ['id', 'name']
        

class BookSerializerList(ModelSerializer):
    
    authors = AuthorSerializerList(many=True)
    shelf = ShelfSerializerList()
    state = BookStateSerializerList()
    availability = BookAvailabilitySerializerList()
    publisher = PublisherSerializerList()
    
    
    class Meta:
        model = Book
        fields = ['id', 'isbn', 'title', 'authors', 'shelf', 'editions', 'state', 'cover', 'publisher', 'availability']
        