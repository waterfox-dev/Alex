import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

import django
django.setup()

from faker import Faker
from server.models import Author, Shelf, BookState, Publisher, Book, User, Loan, LoanToken

fake = Faker()

# Generate fake authors
def generate_authors(num):
    for _ in range(num):
        Author.objects.create(
            first_name=fake.first_name(),
            name=fake.last_name(),
        )

# Generate fake shelves
def generate_shelves(num):
    for _ in range(num):
        Shelf.objects.create(
            name=fake.word(),
            description=fake.text(),
        )

# Generate fake book states
def generate_book_states(num):
    for _ in range(num):
        BookState.objects.create(
            name=fake.word(),
        )

# Generate fake publishers
def generate_publishers(num):
    for _ in range(num):
        Publisher.objects.create(
            name=fake.company(),
        )

# Generate fake books
def generate_books(num):
    for _ in range(num):
        book = Book.objects.create(
            isbn=fake.isbn13(),
            title=fake.sentence(),
            shelf=Shelf.objects.order_by('?').first(),
            availability='AVA',
            state=BookState.objects.order_by('?').first(),
            published_date=fake.date(),
            editions=fake.random_int(min=1, max=10),
            cover=fake.image_url(),
            publisher=Publisher.objects.order_by('?').first(),
        )
        # Assign random authors to the book
        authors_count = fake.random_int(min=1, max=3)
        authors = Author.objects.order_by('?')[:authors_count]
        book.authors.add(*authors)

# Generate fake users 
def generate_users(num):
    for _ in range(num):
        User.objects.create(
            username = fake.user_name(),
            email = fake.email(),
            password = 'password',
            first_name = fake.first_name(),
            last_name = fake.last_name(),
        )

#Generate fake loan 
def generate_loans(num):
    for _ in range(num):
        r_user = User.objects.order_by('?').first()
        r_book = Book.objects.order_by('?').first()
        r_token = LoanToken.create_token(r_user.email, 'password')
        r_book.loan(r_token.token)
        
NUM_AUTHORS = 10
NUM_SHELVES = 5
NUM_BOOK_STATES = 5
NUM_PUBLISHERS = 5
NUM_BOOKS = 30
NUM_USERS = 10
NUM_LOANS = 15 


generate_authors(NUM_AUTHORS)
generate_shelves(NUM_SHELVES)
generate_book_states(NUM_BOOK_STATES)
generate_publishers(NUM_PUBLISHERS)
generate_books(NUM_BOOKS)
generate_users(NUM_USERS) 
generate_loans(NUM_LOANS)

print("Fake data generation completed!")
