from django.contrib import admin

from DjangoProjectRestaurant.review.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'content']
    search_fields = ['user__username', 'content']
