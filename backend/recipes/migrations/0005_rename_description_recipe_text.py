# Generated by Django 3.2 on 2023-07-13 10:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0004_auto_20230713_1504"),
    ]

    operations = [
        migrations.RenameField(
            model_name="recipe",
            old_name="description",
            new_name="text",
        ),
    ]