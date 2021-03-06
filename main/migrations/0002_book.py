# Generated by Django 3.1.3 on 2021-01-18 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('title', models.CharField(max_length=150)),
                ('subtitle', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=5, max_digits=10)),
                ('genre', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=150)),
                ('published_year', models.DateField()),
                ('year_added_to_website', models.DateTimeField()),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
    ]
