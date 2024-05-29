from server.models import User
from server.models import LoanToken
from server.models import Loan
from server.models import Book
from server.models import Shelf
from server.models import BookState
from server.models import Publisher
from server.models import Author

from server.dataclass.api_message import ApiMessage

from django.test import TestCase 

from django.contrib.auth.models import User as DjangoUser

from datetime import datetime

import hashlib
import time


class TestLoanBook(TestCase): 
    
    def setUp(self) -> None:
        User.objects.all().delete()
        Book.objects.all().delete()
        Shelf.objects.all().delete()
        LoanToken.objects.all().delete()
        Loan.objects.all().delete()
        BookState.objects.all().delete()
        Publisher.objects.all().delete()
        Author.objects.all().delete()
        
        self.user = User(
            username='testuser', 
            email='testuser@gmail.com',
            password='12345', 
            first_name='Test',
            last_name='User'
        )     
        
        self.user.save()  
        
        self.shelf = Shelf(
            name='Test Shelf'
        )
        self.shelf.save()
        
        self.state = BookState(
            name='New'
        )
        self.state.save() 
        
        self.publisher = Publisher(
            name='Test Publisher'
        )   
        self.publisher.save() 
        
        self.author = Author(
            name='Author', 
            first_name='Test',  
        )
        self.author.save()
        
        
        self.book = Book(
            isbn=1234567890123,
            title='Test Book',
            shelf=self.shelf,
            state=self.state,
            availability='AVA',
            editions=1,
            publisher=self.publisher,
            published_date=datetime.now(),
        )
        self.book.save()
        self.book.authors.add(self.author)
        
        return super().setUp()
    
    def test_author(self):
        
        admin = DjangoUser.objects.create_superuser('admin', 'admin', 'admin')
        admin.save()
        
        response = self.client.get("http://localhost:8000/api/authors/")
        self.assertEqual(response.status_code, 200)
        
        response = self.client.post(
            "http://localhost:8000/api/authors/", 
            data={"name": "Test", "first_name": "Test"},
        )
        self.assertEqual(response.status_code, 401)
        
        token = self.client.post("http://localhost:8000/api/token", {"username": "admin", "password": "admin"}).json()
        response = self.client.post(
            "http://localhost:8000/api/authors/", 
            HTTP_AUTHORIZATION=f"Bearer {token['access']}", 
            data={"name": "Test", "first_name": "Test"}
        )
        self.assertEqual(response.status_code, 201)