from server.models import Book 
from server.models import Author
from server.models import BookAvailability
from server.models import BookState
from server.models import Shelf
from server.models import Edition

from django.contrib import admin


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookAvailability)
admin.site.register(BookState)
admin.site.register(Shelf)
admin.site.register(Edition)

