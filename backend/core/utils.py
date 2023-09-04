from recipes.models import Ingredient, IngredientRecipe, Recipe
from users.models import User
from django.db.models import QuerySet

def create_ingredients(ingredients: list[dict[int]], recipe: Recipe) -> None:

    ingredients_list = []
    
    for ingredient in ingredients:
        this_ingredient = Ingredient.objects.get(id=ingredient.get("id"))
        amount = ingredient.get("amount")
        ingredients_list.append(
            IngredientRecipe(
                recipe=recipe, ingredient=this_ingredient, amount=amount
            )
        )
    IngredientRecipe.objects.bulk_create(ingredients_list)


def gen_text_cart(user: User, shopping_cart_queryset: QuerySet) -> str:
    
    cart = dict()

    for row_of_shopping_cart in shopping_cart_queryset:
        rows_of_recipe_ingredients = IngredientRecipe.objects.filter(recipe=row_of_shopping_cart.recipe)

        for row_of_recipe_ingredient in rows_of_recipe_ingredients:
            
            ingredient = Ingredient.objects.get
            (
                id=row_of_recipe_ingredient.ingredient.id
            )
            
            name = 
            (
                ingredient.name.capitalize()
                + f" ({ingredient.measurement_unit})"
            )

            res = row_of_recipe_ingredient.amount

            if ingredient.name in cart:

                cart[name] += res

            else:

                cart[name] = res
    

    header = 
    (
        f"""{user.get_full_name()}, Добрый день!
Мы подготовили новый список ингредиентов для покупки."""
    )
    
    footer = "\n\nВаш персональный помощник — Foodgram!"
    
    content = (
        header
        + "\n".join
        (
            [
                f"{igredient_name} — {amount_measurement_unit}"
                for igredient_name, amount_measurement_unit
                in cart.items()
            ]
        ) + footer
    )


    return content
