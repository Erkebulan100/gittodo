from django.db import models
import datetime
# from django_prices.models import MoneyField, TaxedMoneyField


# Create your models here.

class ToDo(models.Model):
    text = models.CharField(max_length = 100)
    created_at = models.DateField(auto_now_add = True)
    is_closed = models.BooleanField(default = False)
    is_favorite = models.BooleanField(default = False)

class Genre(models.Model):
    """Model representing a book genre."""

    name = models.CharField(
        max_length = 200,
        help_text = "Enter a book genre (e.g. Science Fiction, French Poetry etc.)"
    )
class Book(models.Model):
    """ Model representing a book. """
    date_of_adding_the_book_to_the_site = models.DateField(max_length=10)

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=5)    
    # author = models.ForeignKey('Author', on_delete=models.SET_NULL, null = True)
    year = models.IntegerField('year')

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null = True, blank = True)
    class Meta:
        ordering = ['last_name', 'first_name']