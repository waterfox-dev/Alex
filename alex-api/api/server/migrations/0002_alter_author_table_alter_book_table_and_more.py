# Generated by Django 5.0.4 on 2024-04-28 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='author',
            table='alex_demo_author',
        ),
        migrations.AlterModelTable(
            name='book',
            table='alex_demo_book',
        ),
        migrations.AlterModelTable(
            name='bookavailability',
            table='alex_demo_book_availability',
        ),
        migrations.AlterModelTable(
            name='bookstate',
            table='alex_demo_book_state',
        ),
        migrations.AlterModelTable(
            name='edition',
            table='alex_demo_edition',
        ),
        migrations.AlterModelTable(
            name='shelf',
            table='alex_demo_shelf',
        ),
    ]
