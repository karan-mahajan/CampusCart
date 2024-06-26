# Generated by Django 5.0.1 on 2024-02-22 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_category_book_language_book_pages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(blank=True, default='upload_book/book-cover.png', upload_to='upload_book/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(blank=True, choices=[('Fiction', 'Fiction'), ('Non-Fiction', 'Non-Fiction'), ('Academic', 'Academic'), ('Children', 'Children'), ('Art & Photography', 'Art & Photography'), ('Cookbooks', 'Cookbooks'), ('Travel', 'Travel'), ('Health & Wellness', 'Health & Wellness'), ('Religion & Spirituality', 'Religion & Spirituality'), ('Hobbies & Crafts', 'Hobbies & Crafts'), ('Sports & Recreation', 'Sports & Recreation'), ('Science Fiction & Fantasy', 'Science Fiction & Fantasy'), ('Horror', 'Horror'), ('Poetry', 'Poetry'), ('Drama', 'Drama'), ('Others', 'Others')], default='Others', max_length=50),
        ),
    ]
