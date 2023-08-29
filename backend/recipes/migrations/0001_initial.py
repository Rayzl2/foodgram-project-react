# Generated by Django 3.2 on 2023-07-04 09:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Ingredient",
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
                    "name",
                    models.CharField(max_length=64, verbose_name="Название"),
                ),
                (
                    "measurement_unit",
                    models.CharField(
                        max_length=16,
                        verbose_name="Единица измерения",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ингредиент",
                "verbose_name_plural": "Ингредиенты",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="IngredientRecipe",
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
                    "quantity",
                    models.IntegerField(verbose_name="Количество"),
                ),
                (
                    "ingredient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ingredients_recipes",
                        to="recipes.ingredient",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Recipe",
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
                    "name",
                    models.CharField(max_length=128, verbose_name="Название"),
                ),
                (
                    "image",
                    models.ImageField(upload_to="", verbose_name="Картинка"),
                ),
                (
                    "description",
                    models.TextField(verbose_name="Описание"),
                ),
                (
                    "cooking_time",
                    models.IntegerField(verbose_name="Время приготовления"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="recipes",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
                (
                    "ingredients",
                    models.ManyToManyField(
                        through="recipes.IngredientRecipe",
                        to="recipes.Ingredient",
                    ),
                ),
            ],
            options={
                "verbose_name": "Рецепт",
                "verbose_name_plural": "Рецепты",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Tag",
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
                    "name",
                    models.CharField(
                        max_length=64,
                        unique=True,
                        verbose_name="Название",
                    ),
                ),
                (
                    "color",
                    models.CharField(
                        max_length=7,
                        unique=True,
                        verbose_name="Цветовой HEX-код",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=64,
                        unique=True,
                        verbose_name="SLUG",
                    ),
                ),
            ],
            options={
                "verbose_name": "Тег",
                "verbose_name_plural": "Теги",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="TagRecipe",
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
                    "recipe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tags_recipes",
                        to="recipes.recipe",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tags_recipes",
                        to="recipes.tag",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="recipe",
            name="tags",
            field=models.ManyToManyField(
                through="recipes.TagRecipe", to="recipes.Tag"
            ),
        ),
        migrations.AddField(
            model_name="ingredientrecipe",
            name="recipe",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ingredients_recipes",
                to="recipes.recipe",
            ),
        ),
    ]
