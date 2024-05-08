from server.models import User
from server.models import LoanToken
from server.models import Loan
from server.models import Book
from server.models import Shelf
from server.models import BookState
from server.models import Publisher
from server.models import Author

from django.urls import reverse_lazy

from rest_framework.test import APITestCase

from datetime import datetime

import hashlib


class TestLoanTokenApi(APITestCase):
    

    
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
    
    def test_get_token(self):
        response = self.client.post(
            'http://127.0.0.1:8000/api/users/get_loan_token/',
            {
                'mail': 'testuser@gmail.com',
                'password': hashlib.sha256('12345'.encode()).hexdigest()
            }
        )
        
        self.assertEqual(response.status_code,200)
        self.assertIsNotNone(response.data['token'])
        self.assertEqual(response.data['token'], LoanToken.objects.get(user=self.user).token)
        
    def test_get_token_wrong_email(self):
        response = self.client.post(
            'http://127.0.0.1:8000/api/users/get_loan_token/',
            {
                'mail': 'test@gmail.com',
                'password': hashlib.sha256('12345'.encode()).hexdigest()
            }
        )
        
        self.assertEqual(response.status_code,200)
        self.assertIsNone(response.data['token'])
        
    def test_get_token_wrong_email(self):
        response = self.client.post(
            'http://127.0.0.1:8000/api/users/get_loan_token/',
            {
                'mail': 'testuser@gmail.com',
                'password': hashlib.sha256('1234'.encode()).hexdigest()
            }
        )
        
        self.assertEqual(response.status_code,200)
        self.assertIsNone(response.data['token'])
    
    def test_get_token_wrong_email_and_password(self):
        response = self.client.post(
            'http://127.0.0.1:8000/api/users/get_loan_token/',
            {
                'mail': 'test@gmail.com',
                'password': hashlib.sha256('1234'.encode()).hexdigest()
            }
        )
        
        self.assertEqual(response.status_code,200)
        self.assertIsNone(response.data['token'])