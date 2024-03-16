# Generated by Django 5.0.1 on 2024-03-15 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rental',
            name='country',
        ),
        migrations.RemoveField(
            model_name='rental',
            name='state',
        ),
        migrations.AlterField(
            model_name='rental',
            name='address_line2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='rental',
            name='city',
            field=models.CharField(default='Windsor', max_length=100),
        ),
        migrations.AlterField(
            model_name='rental',
            name='description',
            field=models.TextField(),
        ),
    ]
