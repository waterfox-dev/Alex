# Generated by Django 5.0.6 on 2024-05-08 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0011_rename_is_active_user_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loantoken',
            name='lifetime',
            field=models.IntegerField(default=900, help_text='Duration in second for which the token is valid.'),
        ),
    ]
