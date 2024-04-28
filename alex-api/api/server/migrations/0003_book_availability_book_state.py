# Generated by Django 5.0.4 on 2024-04-28 19:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_alter_author_table_alter_book_table_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='availability',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='server.bookavailability'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='state',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='server.bookstate'),
            preserve_default=False,
        ),
    ]
