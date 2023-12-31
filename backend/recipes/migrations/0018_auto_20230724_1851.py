# Generated by Django 3.2 on 2023-07-24 13:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0017_auto_20230723_1010"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ingredientrecipe",
            name="amount",
            field=models.PositiveSmallIntegerField(
                validators=[
                    django.core.validators.MinValueValidator(
                        1, "Количество должно быть больше 0"
                    )
                ],
                verbose_name="Количество",
            ),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="cooking_time",
            field=models.PositiveSmallIntegerField(
                validators=[
                    django.core.validators.MinValueValidator(
                        1, "Время приготовления должно быть больше 0"
                    )
                ],
                verbose_name="Время приготовления",
            ),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="ingredients",
            field=models.ManyToManyField(
                related_name="recipes",
                through="recipes.IngredientRecipe",
                to="recipes.Ingredient",
                verbose_name="Ингредиенты",
            ),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="tags",
            field=models.ManyToManyField(
                related_name="recipes",
                through="recipes.TagRecipe",
                to="recipes.Tag",
                verbose_name="Теги",
            ),
        ),
    ]
