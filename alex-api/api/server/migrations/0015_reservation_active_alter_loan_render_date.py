# Generated by Django 5.0.6 on 2024-05-13 17:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0014_alter_loan_render_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='active',
            field=models.BooleanField(default=True, help_text='Indicates whether the reservation is currently active.'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='render_date',
            field=models.DateField(default=datetime.datetime(2024, 6, 12, 17, 35, 33, 590018, tzinfo=datetime.timezone.utc), help_text='Date when the book must be returned.'),
        ),
    ]