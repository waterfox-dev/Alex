from server.models import User
from server.models import LoanToken
from server.models import Loan
from server.models import Book
from server.models import Shelf
from server.models import BookState
from server.models import Publisher
from server.models import Author

from django.test import TestCase 

from datetime import datetime

import hashlib


class TestLoanToken(TestCase): 
    
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
        self.assertIsNotNone(LoanToken.create_token(
            'testuser@gmail.com', 
            '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5'
        ))    
        
    def test_get_token_wrong_email(self): 
        self.assertIsNone(LoanToken.create_token(
            'test@gmail.com', 
            hashlib.sha256('12345'.encode()).hexdigest()
        ))
    
    def test_get_token_wrong_password(self): 
        self.assertIsNone(LoanToken.create_token(
            'testuser@gmail.com', 
            hashlib.sha256('1234'.encode()).hexdigest()
        ))

    def test_get_token_wrong_email_and_password(self): 
        self.assertIsNone(LoanToken.create_token(
            'test@gmail.com', 
            hashlib.sha256('1234'.encode()).hexdigest()
        ))
        
    def test_loan(self):
        token = LoanToken.create_token(
            'testuser@gmail.com', 
            hashlib.sha256('12345'.encode()).hexdigest()
        )
        self.assertTrue(Loan.loan(token, self.book.id))
        self.assertTrue(Loan.objects.filter(book=self.book).exists())
                
    def test_loan_not_available(self):
        token = LoanToken.create_token(
            'testuser@gmail.com', 
            hashlib.sha256('12345'.encode()).hexdigest()
        )
        self.book.availability = 'LOA'
        self.book.save()
        self.assertFalse(Loan.loan(token, self.book.id))
        self.assertFalse(Loan.objects.filter(book=self.book).exists())
        
    def test_loan_wrong_book(self): 
        token = LoanToken.create_token(
            'testuser@gmail.com', 
            hashlib.sha256('12345'.encode()).hexdigest()
        )
        self.assertFalse(Loan.loan(token, 2))
        self.assertFalse(Loan.objects.filter(book=self.book).exists())
    
    def test_loan_wrong_token(self):    

        self.assertFalse(Loan.loan('wrong_token', self.book.id))
        self.assertFalse(Loan.objects.filter(book=self.book).exists())
        
    def test_return_book(self):
        token = LoanToken.create_token(
            'testuser@gmail.com', 
            hashlib.sha256('12345'.encode()).hexdigest()
        )
        Loan.loan(token, self.book.id)
        self.assertTrue(Loan.return_book(self.book.id))
            