# Generated by Django 3.1.3 on 2021-01-20 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210121_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='go_to_details',
            field=models.BooleanField(default=False),
        ),
    ]
