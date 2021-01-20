from django.db import models
import datetime



# from django_prices.models import MoneyField, TaxedMoneyField


# Create your models here.

class ToDo(models.Model):
    text = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    is_closed = models.BooleanField(default = False)
    is_favorite = models.BooleanField(default = False)

class Book(models.Model):
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150)
    description = models.TextField()
    price = models.TextField()
    genre = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    year = models.DateTimeField(auto_now_add = True)