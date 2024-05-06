from typing import Iterable
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

from datetime import timedelta
from datetime import datetime

from api.settings import DATABASE_TABLE_PREFIX

import hashlib
import random


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


class Publisher(Model): 
    
    class Meta:
        db_table = f'{DATABASE_TABLE_PREFIX}_publisher'
    
    id = AutoField(primary_key=True)
    
    name = CharField(max_length=255) 
        
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True) 
    active =  BooleanField(default=True)
    
    def __str__(self):
        return f'[{self.id}]-{self.name}'

class User(Model): 
    
    class Meta:
        db_table = f'{DATABASE_TABLE_PREFIX}_user'
    
    id = AutoField(primary_key=True)
    
    username = CharField(max_length=255)
    email = CharField(max_length=255, unique=True)
    password = CharField(max_length=255)
    
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    
    is_staff = BooleanField(default=False)
    is_active = BooleanField(default=True)
    is_superuser = BooleanField(default=False)
    
    last_login = DateTimeField(auto_now=True)
    date_joined = DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'[{self.id}]-{self.username} ({self.email})'
    
    def save(self, *args, **kwargs):
        self.password = hashlib.sha256(self.password.encode()).hexdigest()
        super(User, self).save(*args, **kwargs)
    
    @staticmethod 
    def check_password(id: int, password):
        try:
            user = User.objects.get(id=id)
            return password == user.password
        except User.DoesNotExist:
            return False 


class LoanToken(Model):
        
    class Meta:
        db_table = f'{DATABASE_TABLE_PREFIX}_loan_token'
    
    id = AutoField(primary_key=True)
    
    token = CharField(max_length=255)
    user = ForeignKey(User, related_name='loans', on_delete=CASCADE)
    
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True) 
    lifetime = IntegerField(default=7) 
    
        
    def __str__(self):
        return f'[{self.id}]-{self.token}'
    
    @staticmethod 
    def check_token(token:str):
        try:
            loan = LoanToken.objects.get(token=token)
            if loan.created_at + timedelta(minutes=loan.lifetime) > datetime.now():
                return False
            return True
        except LoanToken.DoesNotExist:
            return False
        
    @staticmethod 
    def create_token(mail: str, password: str) -> str:
        try:
            user = User.objects.get(email=mail)
            
            if User.check_password(user.id, password):
                token = hashlib.sha256(f'{mail}-{password}-{datetime.now()}-{random.randint(1, 1024)}'.encode()).hexdigest()
                LoanToken.objects.create(token=token, user=user)
                return token
            return None
        
        except User.DoesNotExist:
            return None


class Loan(Model):
    
    class Meta:
        db_table = f'{DATABASE_TABLE_PREFIX}_loan'
    
    id = AutoField(primary_key=True)
    
    book = ForeignKey('Book', related_name='loans', on_delete=CASCADE)
    token = ForeignKey(LoanToken, related_name='loans', on_delete=CASCADE)
    
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True) 
    active =  BooleanField(default=True)
    
    def __str__(self):
        return f'[{self.id}]-{self.book.title} ({self.token.token})'
    
    @staticmethod 
    def loan(token:str, book_id:int):
        try:
            book = Book.objects.get(id=book_id)
            loan = LoanToken.objects.get(token=token)
            if book.availability == "AVA":
                book.availability = "LOA"
                book.save()
                Loan.objects.create(book=book, token=loan)
                return True
            return False
        except Book.DoesNotExist:
            return False
        except LoanToken.DoesNotExist:
            return False

    @staticmethod 
    def return_book(token:str, book_id:int):
        try:
            book = Book.objects.get(id=book_id)
            loan = LoanToken.objects.get(token=token)
            loan = Loan.objects.get(book=book, token=loan)
            book.availability = "AVA"
            book.save()
            loan.delete()
            return True
        except Book.DoesNotExist:
            return False
        except LoanToken.DoesNotExist:
            return False
        except Loan.DoesNotExist:
            return False

    @staticmethod 
    def get_loans(token:str) -> Iterable['Loan']:
        try:
            loan = LoanToken.objects.get(token=token)
            return Loan.objects.filter(token=loan)
        except LoanToken.DoesNotExist:
            return []
        
    @staticmethod 
    def get_loans_by_book(book_id:int) -> Iterable['Loan']:
        try:
            book = Book.objects.get(id=book_id)
            return Loan.objects.filter(book=book)
        except Book.DoesNotExist:
            return []
        
    @staticmethod 
    def get_loans_by_user(user_id:int) -> Iterable['Loan']:
        try:
            user = User.objects.get(id=user_id)
            return Loan.objects.filter(token__user=user)
        except User.DoesNotExist:
            return []
        
    @staticmethod 
    def get_loan(token:str, book_id:int) -> 'Loan':
        try:
            book = Book.objects.get(id=book_id)
            loan = LoanToken.objects.get(token=token)
            return Loan.objects.get(book=book, token=loan)
        except Book.DoesNotExist:
            return None
        except LoanToken.DoesNotExist:
            return None
        except Loan.DoesNotExist:
            return None    
    
    
class Book(Model): 
    
    class Meta:
        db_table = f'{DATABASE_TABLE_PREFIX}_book'
    
    id = AutoField(primary_key=True)
    
    isbn = BigIntegerField()
    title = CharField(max_length=255) 
    authors = ManyToManyField('Author', related_name='books')
    shelf = ForeignKey('Shelf', related_name='books', on_delete=CASCADE)
    availability = CharField(max_length=255, default='Available', choices=[
        ('AVA', 'Available'), 
        ('LOA', 'Loaned'), 
        ('RES', 'Reserved'), 
        ('LOS', 'Lost'), 
        ('STO', 'In Storage')
    ])
    state = ForeignKey(BookState, related_name='books', on_delete=CASCADE)
    published_date = DateField(null=True, blank=True)
    editions = IntegerField(default=1) 
    cover = URLField(null=True, blank=True)
    publisher = ForeignKey(Publisher, related_name='books', on_delete=CASCADE, null=True, blank=True)
    
    
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True) 
    active =  BooleanField(default=True)

    def __str__(self):
        return f'[{self.id}]-{self.title} ({self.isbn})'
     
    def loan(self, token:str):
        pass