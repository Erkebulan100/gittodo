# Generated by Django 3.1.3 on 2021-01-20 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_book_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.DateTimeField(auto_created=True),
        ),
    ]
