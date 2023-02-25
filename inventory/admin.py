from django.contrib import admin

# Register your models here.
from .models import Inventory


class InventoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'important_number']
    search_fields = ['title', 'content', 'important_number']


admin.site.register(Inventory, InventoryAdmin)
