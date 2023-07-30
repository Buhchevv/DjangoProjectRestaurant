from django.core import validators
from django.db import models

from DjangoProjectRestaurant.users.models import RestaurantUser


class Review(models.Model):
    MAX_CONTENT_LEN = 200
    MIN_CONTENT_LEN = 2
    MIN_RATING_NUM = 1
    MAX_RATING_NUM = 5
    user = models.ForeignKey(
        RestaurantUser,
        on_delete=models.CASCADE,
        default=None,
    )
    content = models.TextField(
        max_length=MAX_CONTENT_LEN,
        validators=(
            validators.MinLengthValidator(MIN_CONTENT_LEN),
        ),
    )
    # rating = models.IntegerField(
    #     blank=True,
    #     null=True,
    #     validators=(
    #         validators.MinLengthValidator(MIN_RATING_NUM),
    #         validators.MaxLengthValidator(MAX_RATING_NUM),
    #     ),
    # )
    # created_at = models.DateTimeField(default=timezone.now())

