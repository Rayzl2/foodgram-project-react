from users.models import Subscribe, User
from django.contrib import admin


admin.site.site_header = "Foodgram Admin"

@admin.register(Subscribe)
class SubscribeConfig(admin.ModelAdmin):

    search_fields = ["subscriber__username", "author__username"]
    list_display = ["id", "subscriber", "author"]
    empty_value_display = "—"

    def get_queryset(self, request):
        queryset = (
            super(SubscribeConfig, self)
            .get_queryset(request)
            .select_related('author', 'subscriber')
        )
        
        return queryset

@admin.register(User)
class UserConfig(admin.ModelAdmin):
    
    list_display = [
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
    ]

    search_fields = ["username", "email"]
    list_display_links = ["id", "username", "email"]
    empty_value_display = "—"
