from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("title", "updated_at")
    search_fields = ("title", "description")

# Register your models here.
