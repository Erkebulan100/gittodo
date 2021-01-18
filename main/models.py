from django.db import models
# from django_prices.models import MoneyField, TaxedMoneyField


# Create your models here.

class ToDo(models.Model):
    text = models.CharField(max_length = 100)
    created_at = models.DateField(auto_now_add = True)
    is_closed = models.BooleanField(default = False)
    is_favorite = models.BooleanField(default = False)

class Book(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=5)
    genre = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    published_year = models.DateField()
    year_added_to_website = models.DateTimeField()
    class Meta:
        ordering = ('-name',)
    def __str__(self):
        return self.name
