from django.contrib import admin

from DjangoProjectRestaurant.reservations.models import TableBooking, AcceptedReservation


@admin.register(TableBooking)
class TableBookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'email', 'date', 'time', 'status']
    search_fields = ['user__username', 'name', 'email']
    list_filter = ['status']
    readonly_fields = ['status']


@admin.register(AcceptedReservation)
class AcceptedReservationAdmin(admin.ModelAdmin):
    list_display = ['reservation', 'accepted_at']
