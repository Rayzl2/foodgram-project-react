from django.core.validators import MinValueValidator
from django.db import models
from users.models import User


class ShoppingCart(models.Model):
    
    user = models.ForeignKey(
        verbose_name="Пользователь",
        to=User,
        on_delete=models.CASCADE,
        related_name="shoppingcarts",
    )

    recipe = models.ForeignKey(
        verbose_name="Рецепт",
        to=Recipe,
        on_delete=models.CASCADE,
        related_name="shoppingcarts",
    )

    class Meta:

        verbose_name_plural = "Списки покупок"
        verbose_name = "Список покупок"
        ordering = ("id",)
        constraints = 
        [
            models.UniqueConstraint(
                fields=["user", "recipe"],
                name="unique_shoppingcart_user_recipe",
            )
        ]

    def __str__(self):
        return (f"""Пользователь {self.user} добавил
                рецепт {self.recipe} в список покупок""")

class Ingredient(models.Model):

    name = models.CharField(verbose_name="Название", max_length=64)
    measurement_unit = models.CharField(
        verbose_name="Единица измерения", max_length=16
    )

    class Meta:
        verbose_name_plural = "Ингредиенты"
        verbose_name = "Ингредиент"
        ordering = ("name",)
        constraints = 
        [
            models.UniqueConstraint(
                fields=["name", "measurement_unit"],
                name="unique_name_measurement_unit",
            )
        ]

    def __str__(self):

        return self.name



class Recipe(models.Model):


    author = models.ForeignKey(
        verbose_name="Автор",
        to=User,
        on_delete=models.CASCADE,
        related_name="recipes",
    )
    name = models.CharField(verbose_name="Название", max_length=128)
    image = models.ImageField(verbose_name="Картинка", max_length=255)
    text = models.TextField(verbose_name="Описание")

    ingredients = models.ManyToManyField(
        Ingredient,
        through="IngredientRecipe",
        verbose_name="Ингредиенты",
        related_name="recipes",
    )

    tags = models.ManyToManyField(
        Tag,
        through="TagRecipe",
        verbose_name="Теги",
        related_name="recipes",
    )

    cooking_time = models.PositiveSmallIntegerField(
        verbose_name="Время приготовления",
        validators=
        [
            MinValueValidator(1, "Время приготовления не может быть равно 0")
        ],
    )

    pub_date = models.DateTimeField(
        verbose_name="Дата публикации", auto_now_add=True
    )

    class Meta:
        verbose_name = "Рецепт"
        ordering = ("-pub_date",)
        verbose_name_plural = "Рецепты"

    def __str__(self):

        return self.name


class IngredientRecipe(models.Model):

    recipe = models.ForeignKey(
        verbose_name="Рецепт",
        to=Recipe,
        on_delete=models.CASCADE,
        related_name="ingredients_recipes",
    )

    ingredient = models.ForeignKey(
        verbose_name="Ингредиент",
        to=Ingredient,
        on_delete=models.CASCADE,
        related_name="ingredients_recipes",
    )

    amount = models.PositiveSmallIntegerField(
        verbose_name="Количество",
        validators=[MinValueValidator(1, "Количество должно быть больше 0")],
    )

    class Meta:
        verbose_name_plural = "Связи рецептов и ингредиентов"
        verbose_name = "Связь рецепта и ингредиента"
        ordering = ("id",)
        constraints = 
        [
            models.UniqueConstraint(
                fields=["recipe", "ingredient"],
                name="unique_recipe_ingredient",
            )
        ]

    def __str__(self):

        return (f"""Рецепт {self.recipe} содержит
                {self.ingredient} в количестве {self.amount}""")


class Tag(models.Model):

    color = models.CharField(verbose_name="Hex-code цвет", max_length=7, unique=True)
    slug = models.SlugField(verbose_name="SLUG", max_length=64, unique=True)
    name = models.CharField(verbose_name="Название", max_length=64, unique=True)

    class Meta:
        verbose_name_plural = "Теги"
        verbose_name = "Тег"
        ordering = ("name",)

    def __str__(self):

        return self.name


class TagRecipe(models.Model):

    tag = models.ForeignKey(
        verbose_name="Тег",
        to=Tag,
        on_delete=models.CASCADE,
        related_name="tags_recipes",
    )


    recipe = models.ForeignKey(
        verbose_name="Рецепт",
        to=Recipe,
        on_delete=models.CASCADE,
        related_name="tags_recipes",
    )


    class Meta:

        verbose_name_plural = "Связи рецептов и тегов"
        verbose_name = "Связь рецепта и тега"
        ordering = ("id",)
        constraints = 
        [
            models.UniqueConstraint(
                fields=["recipe", "tag"], name="unique_recipe_tag"
            )
        ]

    def __str__(self):
        return f"Рецепту {self.recipe} принадлежит тег {self.tag}"


class Favorite(models.Model):

    user = models.ForeignKey(
        verbose_name="Пользователь",
        to=User,
        on_delete=models.CASCADE,
        related_name="favorites",
    )

    recipe = models.ForeignKey(
        verbose_name="Рецепт",
        to=Recipe,
        on_delete=models.CASCADE,
        related_name="favorites",
    )

    class Meta:
        verbose_name_plural = "Списки избранного"
        verbose_name = "Список избранного"
        ordering = ("id",)
        constraints = [
            models.UniqueConstraint(
                fields=["user", "recipe"],
                name="unique_favorite_user_recipe",
            )
        ]

    def __str__(self):

        return (f"""Пользователь {self.user}
                добавил рецепт {self.recipe} в избранное""")


