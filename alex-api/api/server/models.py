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

from django.utils.timezone import datetime
from django.utils.timezone import timedelta 
from django.utils.timezone import now

from api.settings import DATABASE_TABLE_PREFIX

import hashlib
import random
import pytz


class Author(Model):
    """
    Model to represent authors of books.

    Fields:
    - first_name (CharField): First name of the author.
    - name (CharField): Last name of the author.
    - created_at (DateTimeField): Timestamp indicating when the author record was created.
    - updated_at (DateTimeField): Timestamp indicating when the author record was last updated.
    - active (BooleanField): Indicates whether the author is currently active in the system.

    Methods:
    - __str__: Returns a formatted string containing the author's ID, first name, and last name.
    """

    class Meta:
        db_table = f'{DATABASE_TABLE_PREFIX}_author'

    id = AutoField(primary_key=True, help_text="Unique identifier for the author.")
    
    first_name = CharField(max_length=255, help_text="First name of the author.")
    name = CharField(max_length=255, help_text="Last name of the author.")
    
    created_at = DateTimeField(auto_now_add=True, help_text="Timestamp indicating when the author record was created.")
    updated_at = DateTimeField(auto_now=True, help_text="Timestamp indicating when the author record was last updated.")
    active = BooleanField(default=True, help_text="Indicates whether the author is currently active in the system.")

    def __str__(self):
        """
        Returns a formatted string containing the author's ID, first name, and last name.
        """
        return f'[{self.id}]-{self.first_name} {self.name}'
    


class Shelf(Model):
    """
    Model to represent shelves where books are placed.

    Fields:
    - name (CharField): Name of the shelf.
    - description (TextField): Optional description of the shelf.
    - created_at (DateTimeField): Timestamp indicating when the shelf record was created.
    - updated_at (DateTimeField): Timestamp indicating when the shelf record was last updated.
    - active (BooleanField): Indicates whether the shelf is currently active in the system.

    Methods:
    - __str__: Returns a formatted string containing the shelf's ID and name.
    """

    class Meta:
        db_table = f'{DATABASE_TABLE_PREFIX}_shelf'

    id = AutoField(primary_key=True, help_text="Unique identifier for the shelf.")
    
    name = CharField(max_length=255, help_text="Name of the shelf.")
    description = TextField(null=True, blank=True, help_text="Optional description of the shelf.")
        
    created_at = DateTimeField(auto_now_add=True, help_text="Timestamp indicating when the shelf record was created.")
    updated_at = DateTimeField(auto_now=True, help_text="Timestamp indicating when the shelf record was last updated.") 
    active = BooleanField(default=True, help_text="Indicates whether the shelf is currently active in the system.")

    def __str__(self):
        """
        Returns a formatted string containing the shelf's ID and name.
        """
        return f'[{self.id}]-{self.name}'
    
    
class BookState(Model):
    """
    Model to represent the state of books (e.g., new, used, etc.).

    Fields:
    - name (CharField): Name of the book state.
    - created_at (DateTimeField): Timestamp indicating when the book state record was created.
    - updated_at (DateTimeField): Timestamp indicating when the book state record was last updated.
    - active (BooleanField): Indicates whether the book state is currently active in the system.

    Methods:
    - __str__: Returns a formatted string containing the book state's ID and name.
    """

    class Meta:
        db_table = f'{DATABASE_TABLE_PREFIX}_book_state'

    id = AutoField(primary_key=True, help_text="Unique identifier for the book state.")
    
    name = CharField(max_length=255, help_text="Name of the book state.")
        
    created_at = DateTimeField(auto_now_add=True, help_text="Timestamp indicating when the book state record was created.")
    updated_at = DateTimeField(auto_now=True, help_text="Timestamp indicating when the book state record was last updated.") 
    active = BooleanField(default=True, help_text="Indicates whether the book state is currently active in the system.")

    def __str__(self):
        """
        Returns a formatted string containing the book state's ID and name.
        """
        return f'[{self.id}]-{self.name}'


class Publisher(Model):
    """
    Model to represent publishing houses.

    Fields:
    - name (CharField): Name of the publishing house.
    - created_at (DateTimeField): Timestamp indicating when the publisher record was created.
    - updated_at (DateTimeField): Timestamp indicating when the publisher record was last updated.
    - active (BooleanField): Indicates whether the publisher is currently active in the system.

    Methods:
    - __str__: Returns a formatted string containing the publisher's ID and name.
    """

    class Meta:
        db_table = f'{DATABASE_TABLE_PREFIX}_publisher'

    id = AutoField(primary_key=True, help_text="Unique identifier for the publisher.")
    
    name = CharField(max_length=255, help_text="Name of the publishing house.")
        
    created_at = DateTimeField(auto_now_add=True, help_text="Timestamp indicating when the publisher record was created.")
    updated_at = DateTimeField(auto_now=True, help_text="Timestamp indicating when the publisher record was last updated.") 
    active = BooleanField(default=True, help_text="Indicates whether the publisher is currently active in the system.")

    def __str__(self):
        """
        Returns a formatted string containing the publisher's ID and name.
        """
        return f'[{self.id}]-{self.name}'
    

class User(Model):
    """
    Model to represent system users.

    Fields:
    - username (CharField): Username.
    - email (CharField): User's email address.
    - password (CharField): User's password.
    - first_name (CharField): User's first name.
    - last_name (CharField): User's last name.
    - is_staff (BooleanField): Indicates whether the user is a staff member.
    - is_active (BooleanField): Indicates whether the user account is active.
    - is_superuser (BooleanField): Indicates whether the user has superuser privileges.
    - last_login (DateTimeField): Timestamp of the user's last login.
    - date_joined (DateTimeField): Timestamp indicating when the user account was created.

    Methods:
    - __str__: Returns a formatted string containing the user's ID, username, and email address.
    - save: Overrides the save method to hash the user's password before saving.
    - check_password: Static method to check if the provided password matches the user's password.
    """

    class Meta:
        db_table = f'{DATABASE_TABLE_PREFIX}_user'

    id = AutoField(primary_key=True, help_text="Unique identifier for the user.")
    username = CharField(max_length=255, help_text="Username.")
    email = CharField(max_length=255, unique=True, help_text="User's email address.")
    password = CharField(max_length=255, help_text="User's password.")
    first_name = CharField(max_length=255, help_text="User's first name.")
    last_name = CharField(max_length=255, help_text="User's last name.")
    is_staff = BooleanField(default=False, help_text="Indicates whether the user is a staff member.")
    is_superuser = BooleanField(default=False, help_text="Indicates whether the user has superuser privileges.")
    last_login = DateTimeField(auto_now=True, help_text="Timestamp of the user's last login.")
    date_joined = DateTimeField(auto_now_add=True, help_text="Timestamp indicating when the user account was created.")

    active = BooleanField(default=True, help_text="Indicates whether the user account is active.")

    def __str__(self):
        """
        Returns a formatted string containing the user's ID, username, and email address.
        """
        return f'[{self.id}]-{self.username} ({self.email})'

    def save(self, *args, **kwargs):
        """
        Overrides the save method to hash the user's password before saving.
        """
        self.password = hashlib.sha256(self.password.encode()).hexdigest()
        super(User, self).save(*args, **kwargs)

    @staticmethod 
    def check_password(id: int, password):
        """
        Static method to check if the provided password matches the user's password.
        """
        try:
            user = User.objects.get(id=id)
            return password == user.password
        except User.DoesNotExist:
            return False
        

class LoanToken(Model):
    """
    Model to represent tokens used for book loans.

    Fields:
    - token (CharField): Unique token generated for the loan.
    - user (ForeignKey): User associated with the loan token.
    - created_at (DateTimeField): Timestamp indicating when the loan token was created.
    - updated_at (DateTimeField): Timestamp indicating when the loan token was last updated.
    - lifetime (IntegerField): Duration in days for which the token is valid.

    Methods:
    - __str__: Returns a formatted string containing the loan token's ID and token value.
    - check_token: Static method to check if the provided token is valid.
    - create_token: Static method to create a new loan token for a user.
    """

    class Meta:
        db_table = f'{DATABASE_TABLE_PREFIX}_loan_token'

    id = AutoField(primary_key=True, help_text="Unique identifier for the loan token.")
    
    token = CharField(max_length=255, help_text="Unique token generated for the loan.")
    user = ForeignKey('User', related_name='loans', on_delete=CASCADE, help_text="User associated with the loan token.")
    
    created_at = DateTimeField(auto_now_add=True, help_text="Timestamp indicating when the loan token was created.")
    updated_at = DateTimeField(auto_now=True, help_text="Timestamp indicating when the loan token was last updated.") 
    lifetime = IntegerField(default=15*60, help_text="Duration in second for which the token is valid.")
    
    def __str__(self):
        """
        Returns a formatted string containing the loan token's ID and token value.
        """
        return f'[{self.id}]-{self.token}'
    
    @staticmethod 
    def check_token(token:str):
        """
        Static method to check if the provided token is valid.
        """
        try:
            loan = LoanToken.objects.get(token=token)
            if loan.created_at + timedelta(seconds=loan.lifetime) > now():
                return True
            return False
        except LoanToken.DoesNotExist:
            return False
        
    @staticmethod 
    def create_token(mail: str, password: str) -> str:
        """
        Static method to create a new loan token for a user.
        """
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
    """
    Model to represent book loans.

    Fields:
    - book (ForeignKey): Book associated with the loan.
    - token (ForeignKey): Loan token associated with the loan.
    - created_at (DateTimeField): Timestamp indicating when the loan was created.
    - updated_at (DateTimeField): Timestamp indicating when the loan was last updated.
    - active (BooleanField): Indicates whether the loan is currently active.

    Methods:
    - __str__: Returns a formatted string containing the loan's ID, book title, and loan token.
    - loan: Static method to create a new loan for a book using a token.
    - return_book: Static method to mark a loaned book as returned.
    - get_loans: Static method to get all loans associated with a loan token.
    - get_loans_by_book: Static method to get all loans associated with a book.
    - get_loans_by_user: Static method to get all loans associated with a user.
    - get_loan: Static method to get a specific loan by token and book ID.
    """

    class Meta:
        db_table = f'{DATABASE_TABLE_PREFIX}_loan'

    id = AutoField(primary_key=True, help_text="Unique identifier for the loan.")
    
    book = ForeignKey('Book', related_name='loans', on_delete=CASCADE, help_text="Book associated with the loan.")
    token = ForeignKey(LoanToken, related_name='loans', on_delete=CASCADE, help_text="Loan token associated with the loan.")
    
    created_at = DateTimeField(auto_now_add=True, help_text="Timestamp indicating when the loan was created.")
    updated_at = DateTimeField(auto_now=True, help_text="Timestamp indicating when the loan was last updated.") 
    active = BooleanField(default=True, help_text="Indicates whether the loan is currently active.")

    def __str__(self):
        """
        Returns a formatted string containing the loan's ID, book title, and loan token.
        """
        return f'[{self.id}]-{self.book.title} ({self.token.token})'
    
    @staticmethod 
    def loan(token:str, book_id:int):
        """
        Static method to create a new loan for a book using a token.
        """
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
    def return_book(book_id:int):
        """
        Static method to mark a loaned book as returned.
        """
        try:
            book = Book.objects.get(id=book_id)
            loan = Loan.objects.get(book=book, active=True)
            if book.availability == "LOA":
                book.availability = "AVA"
                book.save()
                loan.active = False
                return True
            return False
        except Book.DoesNotExist:
            return False
        except LoanToken.DoesNotExist:
            return False
        except Loan.DoesNotExist:
            return False

    @staticmethod 
    def get_loans(token:str) -> Iterable['Loan']:
        """
        Static method to get all loans associated with a loan token.
        """
        try:
            loan = LoanToken.objects.get(token=token)
            return Loan.objects.filter(token=loan)
        except LoanToken.DoesNotExist:
            return []
        
    @staticmethod 
    def get_loans_by_book(book_id:int) -> Iterable['Loan']:
        """
        Static method to get all loans associated with a book.
        """
        try:
            book = Book.objects.get(id=book_id)
            return Loan.objects.filter(book=book)
        except Book.DoesNotExist:
            return []
        
    @staticmethod 
    def get_loans_by_user(user_id:int, active:bool=True) -> Iterable['Loan']:
        """
        Static method to get all loans associated with a user.
        """
        try:
            user = User.objects.get(id=user_id)
            return Loan.objects.filter(token__user=user, active=active)
        except User.DoesNotExist:
            return []
        
    @staticmethod 
    def get_loan(token:str, book_id:int) -> 'Loan':
        """
        Static method to get a specific loan by token and book ID.
        """
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
    """
    Model to represent books.

    Fields:
    - isbn (BigIntegerField): International Standard Book Number (ISBN) of the book.
    - title (CharField): Title of the book.
    - authors (ManyToManyField): Authors associated with the book.
    - shelf (ForeignKey): Shelf where the book is located.
    - availability (CharField): Availability status of the book.
    - state (ForeignKey): State of the book.
    - published_date (DateField): Date when the book was published.
    - editions (IntegerField): Number of editions of the book.
    - cover (URLField): URL of the book's cover image.
    - publisher (ForeignKey): Publisher of the book.
    - created_at (DateTimeField): Timestamp indicating when the book record was created.
    - updated_at (DateTimeField): Timestamp indicating when the book record was last updated.
    - active (BooleanField): Indicates whether the book is currently active.

    Methods:
    - __str__: Returns a formatted string containing the book's ID, title, and ISBN.
    - loan: Method to create a new loan for the book using a token.
    """

    class Meta:
        db_table = f'{DATABASE_TABLE_PREFIX}_book'

    id = AutoField(primary_key=True, help_text="Unique identifier for the book.")
    
    isbn = CharField(max_length=20, help_text="International Standard Book Number (ISBN) of the book.")
    title = CharField(max_length=255, help_text="Title of the book.")
    authors = ManyToManyField('Author', related_name='books', help_text="Authors associated with the book.")
    shelf = ForeignKey('Shelf', related_name='books', on_delete=CASCADE, help_text="Shelf where the book is located.")
    availability = CharField(max_length=255, default='Available', choices=[
        ('AVA', 'Available'), 
        ('LOA', 'Loaned'), 
        ('RES', 'Reserved'), 
        ('LOS', 'Lost'), 
        ('STO', 'In Storage')
    ], help_text="Availability status of the book.")
    state = ForeignKey(BookState, related_name='books', on_delete=CASCADE, help_text="State of the book.")
    published_date = DateField(null=True, blank=True, help_text="Date when the book was published.")
    editions = IntegerField(default=1, help_text="Number of editions of the book.")
    cover = URLField(null=True, blank=True, help_text="URL of the book's cover image.")
    publisher = ForeignKey(Publisher, related_name='books', on_delete=CASCADE, null=True, blank=True, help_text="Publisher of the book.")
    
    created_at = DateTimeField(auto_now_add=True, help_text="Timestamp indicating when the book record was created.")
    updated_at = DateTimeField(auto_now=True, help_text="Timestamp indicating when the book record was last updated.") 
    active = BooleanField(default=True, help_text="Indicates whether the book is currently active.")

    def __str__(self):
        """
        Returns a formatted string containing the book's ID, title, and ISBN.
        """
        return f'[{self.id}]-{self.title} ({self.isbn})'
     
    def loan(self, token:str):
        """
        Method to create a new loan for the book using a token.
        """
        return Loan.loan(token, self.id)