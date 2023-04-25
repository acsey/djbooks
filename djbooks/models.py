from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.shortcuts import reverse


from django.utils.translation import gettext_lazy as _

# TODO: add multiple images upload

def book_cover_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / slug/<filename>
    return 'djbooks/static/assets/books/libro_{0}/cover_{1}'.format(instance.slug, filename)

def book_back_path(instance, filename):
    return 'djbooks/static/assets/books/libro_{0}/back_{1}'.format(instance.slug, filename)

def book_optional_img1_path(instance, filename):
    return 'djbooks/static/assets/books/libro_{0}/1_{1}'.format(instance.slug, filename)

def book_optional_img2_path(instance, filename):
    return 'djbooks/static/assets/books/libro_{0}/2_{1}'.format(instance.slug, filename)

class Book(models.Model):
    class Category(models.TextChoices):
        book = 'L', _('Libros')
        old_book = 'LA', _('Libros Antiguos')
        signed_book = 'LF', _('Libros Firmados')
        first_edition = 'PE', _('Primeras Ediciones')
    # TODO: Refactor this to use a many to many relationship
    category = models.CharField(
        max_length=2,
        choices=Category.choices,
        default=Category.book,
    )
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    editorial = models.CharField(max_length=30)
    editon = models.CharField(max_length=20)
    year = models.CharField(max_length=4)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    cover = models.ImageField(upload_to=book_cover_path)
    back = models.ImageField(upload_to=book_back_path, default=None, null=True)
    optional_img1 = models.ImageField(upload_to=book_optional_img1_path, default=None, null=True)
    optional_img2 = models.ImageField(upload_to=book_optional_img2_path, default=None, null=True)
    description = models.TextField(default=None, null=True)
    condition = models.TextField(default=None, null=True)
    stock = models.IntegerField(default=1)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.title
    
    @classmethod
    def get_category_labels(cls):
        return cls.Category.labels
    
    @classmethod
    def get_book_categories_count(cls):
        books = dict()
        for value, label in cls.Category.choices:
            books[label] = cls.objects.filter(category=value).count()
        return books

    def get_absolute_url(self):
        return reverse("djbooks:book_detail", kwargs={"slug": self.slug})

    def get_add_to_cart_url(self):
        return reverse("djbooks:add-to-cart", kwargs={"slug": self.slug})

    def get_remove_from_cart_url(self):
        return reverse("djbooks:remove-from-cart", kwargs={"slug": self.slug})


class OrderBook(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(OrderBook)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)

    """
    1. Book added to cart
    2. Adding a billing address (Failed checkout)
    3. Payment (Preprocessing, processing, packaging etc.)
    4. Being delivered
    5. Received
    6. Refunds
    """

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total

