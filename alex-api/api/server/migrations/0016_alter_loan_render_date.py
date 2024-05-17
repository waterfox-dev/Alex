# Generated by Django 5.0.6 on 2024-05-17 17:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0015_reservation_active_alter_loan_render_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='render_date',
            field=models.DateField(default=datetime.datetime(2024, 6, 16, 17, 31, 15, 445828, tzinfo=datetime.timezone.utc), help_text='Date when the book must be returned.'),
        ),
    ]