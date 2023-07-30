from enum import Enum

from django.db import models


class ChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class MenuItems(ChoicesEnum):
    STARTERS = 'Starters'
    SALADS = 'Salads'
    SPECIALTY = 'Specialty'


class MenuItem(models.Model):
    MAX_LEN_TITLE = 100
    MAX_LEN_DESCRIPTION = 255
    MAX_LEN_CATEGORY = 50

    title = models.CharField(
        max_length=MAX_LEN_TITLE
    )
    description = models.TextField(
        max_length=MAX_LEN_DESCRIPTION,
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    category = models.CharField(
        max_length=MAX_LEN_CATEGORY,
        choices=MenuItems.choices(),
        null=False,
        blank=False,

    )
    menu_image = models.ImageField(
        upload_to='menu_items',
        null=True,
        blank=True,
    )
    ingredients = models.TextField(
    )
    available = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.title
