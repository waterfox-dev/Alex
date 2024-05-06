from server.models import User
from server.models import LoanToken

from unittest import TestCase 

import hashlib


class TestLoanToken(TestCase): 
    
    def setUp(self) -> None:
        User.objects.all().delete()
        user = User(
            username='testuser', 
            email='testuser@gmail.com',
            password='12345', 
            first_name='Test',
            last_name='User'
        )       
        user.save()
        return super().setUp()
    
    def test_get_token(self): 
        self.assertIsNotNone(LoanToken.create_token(
            'testuser@gmail.com', 
            hashlib.sha256('12345'.encode()).hexdigest()
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