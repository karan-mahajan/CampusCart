# Generated by Django 5.0.1 on 2024-03-18 15:02

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LostandfoundItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[("LOST", "Lost"), ("FOUND", "Found")], max_length=5
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("product_description", models.TextField()),
                ("post_date", models.DateTimeField(auto_now_add=True)),
                ("image", models.ImageField(upload_to="lost_and_found_images/")),
                ("location", models.CharField(max_length=100)),
            ],
        ),
    ]
