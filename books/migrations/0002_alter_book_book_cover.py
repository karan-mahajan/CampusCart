# Generated by Django 5.0.1 on 2024-02-17 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(default='book-cover.png', upload_to='upload_book/'),
        ),
    ]