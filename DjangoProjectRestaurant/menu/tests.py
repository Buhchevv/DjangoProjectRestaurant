from django.test import TestCase

from DjangoProjectRestaurant.menu.models import MenuItem


class MenuItemModelTest(TestCase):

    def setUp(self):
        self.menu_item = MenuItem.objects.create(
            title='Test Item',
            description='This is a test item.',
            price=10.99,
            category='Starters',
            ingredients='Ingredient 1, Ingredient 2',
            available=True,
        )

    def test_menu_item_content(self):
        self.assertEqual(str(self.menu_item), 'Test Item')
        self.assertEqual(self.menu_item.description, 'This is a test item.')
        self.assertEqual(self.menu_item.price, 10.99)
        self.assertEqual(self.menu_item.category, 'Starters')
        self.assertEqual(
            self.menu_item.ingredients, 'Ingredient 1, Ingredient 2')
        self.assertTrue(self.menu_item.available)
