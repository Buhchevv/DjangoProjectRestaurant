from django.contrib import admin

from DjangoProjectRestaurant.subscribers.models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'date_subscribed']
    search_fields = ['email']