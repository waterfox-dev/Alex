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
    
    secure_list = [
        "http://127.0.0.1:8000/api/authors/"
    ]

    def test_forbiden(self):
        for url in self.secure_list:
            response = self.client.post(url)
            self.assertEqual(response.status_code, 403)
            
    def test_authorized(self):
        for url in self.secure_list:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)