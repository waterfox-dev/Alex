from server.models import User
from server.models import LoanToken
from server.models import Loan
from server.models import Book
from server.models import Shelf
from server.models import BookState
from server.models import Publisher
from server.models import Author
from server.models import Reservation

from server.dataclass.api_message import ApiMessage

from django.test import TestCase 

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
    
    def test_loan_book(self) : 
        token = LoanToken.create_token(
            'testuser@gmail.com', 
           '12345'   
        )
        self.assertIsNotNone(token)
        self.assertEqual(token.user, self.user) 
        
        loan = Book.objects.get(id=1).loan(token.token)
        self.assertEqual(Book.objects.get(id=1).availability, 'LOA')
        self.assertEqual(loan.status, 100)
          
    def test_loan_book_wrong_token(self) : 
        token = LoanToken.create_token(
            'testuser@gmail.com', 
            '1234'   
        )
        self.assertIsNone(token) 
    
    def test_loan_book_already_loaned(self) : 
        self.book.availability = 'LOA'
        self.book.save()
        
        token = LoanToken.create_token(
            'testuser@gmail.com', 
            '12345'   
        )
        self.assertIsNotNone(token)
        self.assertEqual(token.user, self.user)
        
        loan = Book.objects.get(id=1).loan(token.token)
        self.assertEqual(loan.status, 200)
    
    def test_loan_book_in_stock(self) : 
        self.book.availability = 'STO'
        self.book.save()
        
        token = LoanToken.create_token(
            'testuser@gmail.com', 
            '12345' 
        )
        self.assertIsNotNone(token)
        
        loan = Book.objects.get(id=1).loan(token.token)
        self.assertEqual(loan.status, 1001)
        
            