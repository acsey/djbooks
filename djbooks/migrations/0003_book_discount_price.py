# Generated by Django 4.1.7 on 2023-03-11 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djbooks', '0002_book_condition_book_editon_book_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]