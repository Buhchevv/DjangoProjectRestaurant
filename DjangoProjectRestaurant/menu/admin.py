from django.contrib import admin

from DjangoProjectRestaurant.menu.models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category', 'available']
    search_fields = ['title', 'category']
    list_filter = ['category', 'available']
