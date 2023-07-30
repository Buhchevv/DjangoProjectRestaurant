from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views import View

from DjangoProjectRestaurant import settings
from DjangoProjectRestaurant.reservations.forms import TableBookingForm
from DjangoProjectRestaurant.reservations.models import TableBooking


@login_required
def book_table(request):
    if request.method == 'POST':
        form = TableBookingForm(request.POST)
        if form.is_valid():
            table_booking = form.save(commit=False)
            table_booking.user = request.user
            table_booking.save()
            return redirect('booking confirmation')
    else:
        form = TableBookingForm(user=request.user)

    context = {
        'form': form
    }
    return render(request, 'booking/book_table-page.html', context)


class ReservationsView(LoginRequiredMixin, UserPassesTestMixin, View):

    def test_func(self):
        return self.request.user.is_staff

    def get(self, request):
        reservations = TableBooking.objects.all()
        context = {
            'reservations': reservations
        }
        return render(request, 'reservations/all_reservations.html', context)


class AcceptReservationsView(LoginRequiredMixin, UserPassesTestMixin, View):

    def test_func(self):
        return self.request.user.is_staff

    def post(self, request, pk):
        reservation = get_object_or_404(TableBooking, pk=pk)

        reservation.status = 'Accepted'
        reservation.save()

        subject = 'Reservation Accepted'
        message = render_to_string('reservations/accept_email.html', {'reservation': reservation})
        plain_message = strip_tags(message)
        from_email = settings.EMAIL_HOST_USER
        to_email = reservation.email

        send_mail(subject, plain_message, from_email, [to_email], html_message=message)

        return redirect('all reservations')


class DeclineReservationsView(LoginRequiredMixin, UserPassesTestMixin, View):

    def test_func(self):
        return self.request.user.is_staff

    def post(self, request, pk):
        reservation = get_object_or_404(TableBooking, pk=pk)

        subject = 'Reservation Declined'
        message = render_to_string('reservations/decline_email.html', {'reservation': reservation})
        plain_message = strip_tags(message)
        from_email = settings.EMAIL_HOST_USER
        to_email = reservation.email

        send_mail(subject, plain_message, from_email, [to_email], html_message=message)

        reservation.delete()

        return redirect('all reservations')


class DeleteReservationView(LoginRequiredMixin, UserPassesTestMixin, View):

    def test_func(self):
        return self.request.user.is_staff

    def post(self, request, pk):
        reservation = get_object_or_404(TableBooking, pk=pk)
        reservation.delete()
        return redirect('all reservations')


def booking_confirmation(request):
    return render(request, 'booking/booking_confirmation.html')
