# Generated by Django 3.1.3 on 2021-01-20 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_book_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='price',
            new_name='cost',
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
