# Generated by Django 3.1.3 on 2021-01-20 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210120_1052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='price1',
            new_name='price',
        ),
    ]
