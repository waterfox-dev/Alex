# Generated by Django 5.0.4 on 2024-04-28 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_alter_book_isbn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='authors',
        ),
    ]
