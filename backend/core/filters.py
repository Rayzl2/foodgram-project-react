from admin_auto_filters.filters import AutocompleteFilter


class AuthorFilter(AutocompleteFilter):
    title = "Автор"
    field_name = "author"


class IngredientsFilter(AutocompleteFilter):
    title = "Ингредиент"
    field_name = "ingredients"


class TagsFilter(AutocompleteFilter):
    title = "Тег"
    field_name = "tags"