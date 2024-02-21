# Generated by Django 4.2.10 on 2024-02-18 12:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0004_remove_product_interested_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="interested_users",
            field=models.ManyToManyField(
                related_name="interested_products", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]