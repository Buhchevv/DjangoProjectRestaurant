from django.contrib import admin

from DjangoProjectRestaurant.contact.models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']
    search_fields = ['name', 'email', 'subject']