import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

import django
django.setup()

from faker import Faker
from server.models import Author, Shelf, BookState, Publisher, Book

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
            availability=fake.random_element(elements=['AVA', 'LOA', 'RES', 'LOS', 'STO']),
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

NUM_AUTHORS = 10
NUM_SHELVES = 5
NUM_BOOK_STATES = 5
NUM_PUBLISHERS = 5
NUM_BOOKS = 20

generate_authors(NUM_AUTHORS)
generate_shelves(NUM_SHELVES)
generate_book_states(NUM_BOOK_STATES)
generate_publishers(NUM_PUBLISHERS)
generate_books(NUM_BOOKS)

print("Fake data generation completed!")
