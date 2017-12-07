from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    name = models.CharField(max_length=512)


class Book(models.Model):
    title = models.CharField(max_length=512)
    author = models.CharField(max_length=256)
    categories = models.ManyToManyField(Category, related_name='books')
    cover_image = models.ImageField(upload_to='covers')
    link = models.URLField(max_length=512, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)


class Resource(models.Model):
    title = models.CharField(max_length=512)
    short_description = models.CharField(max_length=2048, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(max_length=512, blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    email = models.EmailField()
