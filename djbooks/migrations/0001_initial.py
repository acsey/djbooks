# Generated by Django 4.1.7 on 2023-03-27 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djbooks.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('L', 'Libros'), ('LA', 'Libros Antiguos'), ('LF', 'Libros Firmados'), ('LI', 'Libros Infantiles'), ('PE', 'Primeras Ediciones')], default='L', max_length=2)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=30)),
                ('editorial', models.CharField(max_length=30)),
                ('editon', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=4)),
                ('price', models.FloatField()),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('cover', models.ImageField(upload_to=djbooks.models.book_cover_path)),
                ('back', models.ImageField(default=None, null=True, upload_to=djbooks.models.book_back_path)),
                ('optional_img1', models.ImageField(default=None, null=True, upload_to=djbooks.models.book_optional_img1_path)),
                ('optional_img2', models.ImageField(default=None, null=True, upload_to=djbooks.models.book_optional_img2_path)),
                ('description', models.TextField(default=None, null=True)),
                ('condition', models.TextField(default=None, null=True)),
                ('stock', models.IntegerField(default=1)),
                ('slug', models.SlugField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djbooks.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(blank=True, max_length=20, null=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('being_delivered', models.BooleanField(default=False)),
                ('received', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(to='djbooks.orderbook')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
