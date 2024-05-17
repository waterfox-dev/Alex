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
import time


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
            '12345'
        ))    
        
    def test_get_token_wrong_email(self): 
        self.assertIsNone(LoanToken.create_token(
            'test@gmail.com', 
            '12345'
        ))
    
    def test_get_token_wrong_password(self): 
        self.assertIsNone(LoanToken.create_token(
            'testuser@gmail.com', 
            '1234'
        ))

    def test_get_token_wrong_email_and_password(self): 
        self.assertIsNone(LoanToken.create_token(
            'test@gmail.com', 
            '1234'
        ))
        
    def test_loan(self):
        token = LoanToken.create_token(
            'testuser@gmail.com', 
            '12345'
        )
        self.assertTrue(Loan.loan(token.token, self.book.id))
        self.assertTrue(Loan.objects.filter(book=self.book).exists())
                
    def test_loan_not_available(self):
        token = LoanToken.create_token(
            'testuser@gmail.com', 
            '12345'
        )
        self.book.availability = 'LOA'
        self.book.save()
        self.assertEqual(Loan.loan(token.token, self.book.id).status, 101)
        self.assertFalse(Loan.objects.filter(book=self.book).exists())
        
    def test_loan_wrong_book(self): 
        token = LoanToken.create_token(
            'testuser@gmail.com', 
            '12345'
        )
        self.assertEqual(Loan.loan(token.token, 2).status, 102)
        self.assertFalse(Loan.objects.filter(book=self.book).exists())
    
    def test_loan_wrong_token(self):    

        self.assertEqual(Loan.loan('wrong_token', self.book.id).status, 103)
        self.assertFalse(Loan.objects.filter(book=self.book).exists())
        
    def test_return_book(self):
        token = LoanToken.create_token(
            'testuser@gmail.com', 
            '12345'
        )
        Loan.loan(token.token, self.book.id)
        self.assertTrue(Loan.return_book(self.book.id))
            
    def test_token_expired(self):
        token = LoanToken.create_token(
            'testuser@gmail.com',  
           '12345'
        )
        token = LoanToken.objects.get(token=token.token)
        token.lifetime = 1
        token.save()
        time.sleep(1)
        self.assertFalse(LoanToken.check_token(token.token))