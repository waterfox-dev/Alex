from django.db.models import Model 

from django.db.models import CharField 
from django.db.models import DateTimeField
from django.db.models import IntegerField
from django.db.models import BigIntegerField
from django.db.models import URLField
from django.db.models import BooleanField
from django.db.models import TextField
from django.db.models import AutoField
from django.db.models import DateField
  
from django.db.models import CASCADE  
  
from django.db.models import ForeignKey
from django.db.models import ManyToManyField    

from api.settings import DATABASE_TABLE_PREFIX

class Author(Model): 
    
    class Meta:
        db_table = f'{DATABASE_TABLE_PREFIX}_author'
    
    id = AutoField(primary_key=True)
    
    first_name = CharField(max_length=255)
    name = CharField(max_length=255) 
    
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True) 
    active =  BooleanField(default=True)
    
    def __str__(self):
        return f'[{self.id}]-{self.first_name} {self.name}'

class Shelf(Model): 
    
    class Meta:
        db_table = f'{DATABASE_TABLE_PREFIX}_shelf'
    
    id = AutoField(primary_key=True)
    
    name = CharField(max_length=255) 
    description = TextField(null=True, blank=True)
        
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True) 
    active =  BooleanField(default=True)
    
    def __str__(self):
        return f'[{self.id}]-{self.name}'
    

class BookAvailability(Model): 
    
    class Meta:
        db_table = f'{DATABASE_TABLE_PREFIX}_book_availability'
    
    id = AutoField(primary_key=True)
    
    name = CharField(max_length=255) 
        
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True) 
    active =  BooleanField(default=True)
    
    def __str__(self):
        return f'[{self.id}]-{self.name}'

class BookState(Model):
        
    class Meta:
        db_table = f'{DATABASE_TABLE_PREFIX}_book_state'    
        
    id = AutoField(primary_key=True)
    
    name = CharField(max_length=255) 
        
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True) 
    active =  BooleanField(default=True)
    
    def __str__(self):
        return f'[{self.id}]-{self.name}'


class Book(Model): 
    
    class Meta:
        db_table = f'{DATABASE_TABLE_PREFIX}_book'
    
    id = AutoField(primary_key=True)
    
    isbn = BigIntegerField()
    title = CharField(max_length=255) 
    author = ManyToManyField('Author', related_name='books')
    shelf = ForeignKey('Shelf', related_name='books', on_delete=CASCADE)
    availability = ForeignKey(BookAvailability, related_name='books', on_delete=CASCADE)
    state = ForeignKey(BookState, related_name='books', on_delete=CASCADE)
    
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True) 
    active =  BooleanField(default=True)

    def __str__(self):
        return f'[{self.id}]-{self.title} ({self.isbn})'

class Edition(Model): 
    
    class Meta:
        db_table = f'{DATABASE_TABLE_PREFIX}_edition'
    
    id = AutoField(primary_key=True)
    
    name = CharField(max_length=255)
    publisher = CharField(max_length=255)
    publication_date = DateField()
    book = ForeignKey('Book', related_name='editions', on_delete=CASCADE)
    cover = URLField(null=True, blank=True)
    
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True) 
    active =  BooleanField(default=True)
    
    def __str__(self):
        return f'[{self.id}]-{self.name} ({self.publisher})'
