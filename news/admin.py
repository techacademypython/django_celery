from django.contrib import admin
from .models import Data, Token

# Register your models here.
admin.site.register(Data)


class TokenAdmin(admin.ModelAdmin):
    list_display = ["token", "user", "expire", "create_date"]


admin.site.register(Token, TokenAdmin)
