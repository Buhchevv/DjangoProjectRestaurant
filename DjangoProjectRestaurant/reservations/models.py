from datetime import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.db import models

from DjangoProjectRestaurant.users.models import RestaurantUser


class TableBooking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
    )

    user = models.ForeignKey(
        RestaurantUser,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=255,
        blank=False
    )
    email = models.EmailField(
        blank=False
    )
    phone = models.CharField(
        max_length=20,
        blank=False
    )
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.PositiveIntegerField(
        validators=[MaxValueValidator(
            120, 'The number of people exceeds the maximum capacity'
        )]
    )
    message = models.TextField(
        blank=True,
        null=True,
    )

    def clean(self):
        expected_format = '%d/%m/%Y'
        if self.date is not None:
            try:
                self.date = datetime.strptime(self.date.strftime(expected_format), expected_format).date()
            except ValueError:
                raise ValidationError({
                    'date': 'Invalid date format. Please enter a date in the format DD/MM/YYYY.'
                })

    def __str__(self):
        return self.name


class AcceptedReservation(models.Model):
    reservation = models.OneToOneField(
        TableBooking,
        on_delete=models.CASCADE,
        related_name='accepted_reservation'
    )
    accepted_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Accepted Reservation for {self.reservation.name}"
