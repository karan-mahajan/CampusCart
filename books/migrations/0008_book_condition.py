# Generated by Django 5.0.1 on 2024-03-24 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_bookviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='condition',
            field=models.CharField(choices=[('New', 'New'), ('Used', 'Used')], default='New', max_length=255),
        ),
    ]
