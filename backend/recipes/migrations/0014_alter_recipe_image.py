# Generated by Django 3.2 on 2023-07-22 17:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0013_auto_20230722_0816"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="image",
            field=models.ImageField(
                max_length=500, upload_to="", verbose_name="Картинка"
            ),
        ),
    ]
