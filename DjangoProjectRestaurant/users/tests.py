from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class RestaurantUserModelTest(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(
            username='test_user',
            email='test@example.com',
            password='test_password',
        )
        self.assertEqual(user.username, 'test_user')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('test_password'))

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin_password',
        )
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
