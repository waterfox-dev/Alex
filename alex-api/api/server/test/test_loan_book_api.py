from server.models import User
from server.models import LoanToken
from server.models import Loan
from server.models import Book
from server.models import Shelf
from server.models import BookState
from server.models import Publisher
from server.models import Author

from rest_framework.test import APITestCase

from datetime import datetime

import hashlib


class TestLoanBookApi(APITestCase):
    

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
    
    def test_loan_book(self) :
        response = self.client.post(
            'http://127.0.0.1:8000/api/users/get_loan_token/',
            {
                'mail': 'testuser@gmail.com',
                'password': hashlib.md5('12345'.encode()).hexdigest()
            }
        )
        token = response.data['token'] 
        response = self.client.post(
            'http://127.0.0.1:8000/api/books/1/loan/',
            {
                'token': token      
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], 1)
        
    def test_loan_book_no_token(self) :
        response = self.client.post(
            'http://127.0.0.1:8000/api/books/1/loan/'
        )
        self.assertEqual(response.status_code, 400)
        
    def test_loan_book_wrong_token(self) :
        response = self.client.post(
            'http://127.0.0.1:8000/api/books/1/loan/',
            {
                'token': 'wrong_token'
            }
        )
        self.assertEqual(response.status_code, 400)
        
    def test_loan_book_already_loaned(self) :
        self.book.availability = 'LOA'
        self.book.save()
        
        response = self.client.post(
            'http://127.0.0.1:8000/api/users/get_loan_token/',
            {
                'mail': 'testuser@gmail.com',
                'password': hashlib.md5('12345'.encode()).hexdigest()
            }
        )
        token = response.data['token'] 
        response = self.client.post(
            'http://127.0.0.1:8000/api/books/1/loan/',
            {
                'token': token      
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], 2)
        