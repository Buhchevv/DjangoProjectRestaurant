from django.contrib import admin

from DjangoProjectRestaurant.users.models import RestaurantUser


@admin.register(RestaurantUser)
class RestaurantUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    list_filter = ['is_staff', 'is_active', 'groups']
    readonly_fields = ['date_joined']