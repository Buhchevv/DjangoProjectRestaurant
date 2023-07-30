from django.urls import path, include


from DjangoProjectRestaurant.reservations.views import booking_confirmation, book_table, ReservationsView, \
    AcceptReservationsView, DeclineReservationsView, DeleteReservationView

urlpatterns = [
                  path('booking-confirmation/', booking_confirmation, name='booking confirmation'),
                  path('table-booking/', book_table, name='booking table page'),
                  path('all-reservations/', include([
                      path('', ReservationsView.as_view(), name='all reservations'),
                      path('accept/<int:pk>/', AcceptReservationsView.as_view(), name='accept reservation'),
                      path('decline/<int:pk>/', DeclineReservationsView.as_view(), name='decline reservation'),
                      path('delete/<int:pk>/', DeleteReservationView.as_view(), name='delete reservation'),
                  ])),
              ]

