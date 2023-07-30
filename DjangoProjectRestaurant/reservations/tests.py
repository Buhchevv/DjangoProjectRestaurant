from datetime import datetime, time

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from DjangoProjectRestaurant.reservations.models import AcceptedReservation, TableBooking

User = get_user_model()


class TableBookingModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user',
            email='test@example.com',
            password='test_password',
        )
        self.booking = TableBooking.objects.create(
            user=self.user,
            name='Test User',
            email='test@example.com',
            phone='1234567890',
            date='2023-07-10',
            time='13:30:00',
            number_of_people=4,
            message='This is a test booking.'
        )

    def test_booking_content(self):
        self.assertEqual(str(self.booking), 'Test User')
        self.assertEqual(self.booking.user, self.user)
        self.assertEqual(self.booking.status, 'pending')
        self.assertEqual(self.booking.email, 'test@example.com')
        self.assertEqual(self.booking.phone, '1234567890')
        self.assertEqual(self.booking.date, '2023-07-10')
        self.assertEqual(self.booking.time, '13:30:00')
        self.assertEqual(self.booking.number_of_people, 4)
        self.assertEqual(self.booking.message, 'This is a test booking.')


class AcceptedReservationModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user',
            email='test@example.com',
            password='test_password',
        )
        self.booking = TableBooking.objects.create(
            user=self.user,
            name='Test User',
            email='test@example.com',
            phone='1234567890',
            date='2023-07-10',
            time='13:30:00',
            number_of_people=4,
            message='This is a test booking.'
        )
        self.accepted_reservation = AcceptedReservation.objects.create(
            reservation=self.booking,
        )

    def test_accepted_reservation_content(self):
        self.assertEqual(
            str(self.accepted_reservation), 'Accepted Reservation for Test User')
        self.assertEqual(self.accepted_reservation.reservation, self.booking)

    def test_table_booking_page_post_valid_form(self):
        user = User.objects.create_user(username='test_user', password='test_pass')

        self.client.login(username='test_user', password='test_pass')

        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '123456789',
            'date': '2023-07-10',
            'time': '14:00:00',
            'number_of_people': 4,
            'message': 'Test booking'
        }

        data['date'] = datetime.strptime(data['date'], '%Y-%m-%d').date()
        data['time'] = datetime.strptime(data['time'], '%H:%M:%S').time()

        response = self.client.post(reverse('booking table page'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('booking confirmation'))

        self.assertEqual(TableBooking.objects.count(), 1)
        table_booking = TableBooking.objects.first()

        self.assertEqual(table_booking.name, 'John Doe')
        self.assertEqual(table_booking.email, 'john@example.com')
        self.assertEqual(table_booking.phone, '123456789')
        self.assertEqual(table_booking.date, datetime.strptime('2023-07-10', '%Y-%m-%d').date())
        self.assertEqual(table_booking.time, time(14, 0))
        self.assertEqual(table_booking.number_of_people, 4)
        self.assertEqual(table_booking.message, 'Test booking')

    def test_table_booking_page_post_invalid_form(self):
        user = User.objects.create_user(username='test_user', password='test_pass')

        self.client.login(username='test_user', password='test_pass')

        data = {
            'name': '',
            'email': '',
            'phone': '',
            'date': '',
            'time': '',
            'number_of_people': -1,
            'message': ''
        }
        response = self.client.post(reverse('booking table page'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/book_table-page.html')
        self.assertFormError(response, 'form', 'name', 'This field is required.')
        self.assertFormError(response, 'form', 'email', 'This field is required.')
        self.assertFormError(response, 'form', 'phone', 'This field is required.')
        self.assertFormError(response, 'form', 'date', 'This field is required.')
        self.assertFormError(response, 'form', 'time', 'This field is required.')
        self.assertFormError(response, 'form', 'number_of_people', 'Ensure this value is greater than or equal to 0.')
