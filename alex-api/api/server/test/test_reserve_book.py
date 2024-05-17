from server.models import User
from server.models import LoanToken
from server.models import Loan
from server.models import Book
from server.models import Shelf
from server.models import BookState
from server.models import Publisher
from server.models import Author
from server.models import Reservation

from api.settings import ALEX_LOAN_DURATION

from django.test import TestCase 

from datetime import datetime
from datetime import timedelta

import hashlib
import time


class TestReserveBook(TestCase): 
    
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
    
    def test_reserve_book(self): 
        self.book.availability = 'LOA'
        self.book.save()
        
        token = LoanToken.create_token(
            'testuser@gmail.com', 
            '12345'   
        ) 
        
        self.assertIsNotNone(token)
        self.assertEqual(token.user, self.user) 
    
        loan = Book.objects.get(id=1).loan(token.token)
        self.assertEqual(Book.objects.get(id=1).availability, 'RES')
        self.assertEqual(loan.status, 200)

    def test_reserve_book_already_reserved(self): 
        self.book.availability = 'RES'
        self.book.save()
        
        token = LoanToken.create_token(
            'testuser@gmail.com', 
            '12345'    
        ) 
        
        self.assertIsNotNone(token)
        self.assertEqual(token.user, self.user) 
    
        loan = Book.objects.get(id=1).loan(token.token)
        self.assertEqual(Book.objects.get(id=1).availability, 'RES')
        self.assertEqual(loan.status, 200)
        
    def test_reservation_duration(self): 
        self.book.availability = 'LOA'
        self.book.save()
        
        token = LoanToken.create_token(
            'testuser@gmail.com', 
            '12345'    
        ) 
        
        self.assertIsNotNone(token)
        self.assertEqual(token.user, self.user) 
    
        Book.objects.get(id=1).loan(token.token)
        reservation_response = Book.objects.get(id=1).loan(token.token)
        reservation = Reservation.objects.filter(book=Book.objects.get(id=1)).order_by('-availability_date')[0]

        self.assertEqual(Book.objects.get(id=1).availability, 'RES')
        self.assertEqual(reservation.availability_date.day, (datetime.now().date() + timedelta(days=ALEX_LOAN_DURATION*2)).day)
        self.assertEqual(reservation.availability_date.month, (datetime.now().date() + timedelta(days=ALEX_LOAN_DURATION*2)).month)
        self.assertEqual(reservation.availability_date.year, (datetime.now().date() + timedelta(days=ALEX_LOAN_DURATION*2)).year)
        self.assertEqual(reservation_response.status, 200)    