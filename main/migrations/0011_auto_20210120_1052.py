# Generated by Django 3.1.3 on 2021-01-20 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210120_1045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='cost',
            new_name='price1',
        ),
    ]