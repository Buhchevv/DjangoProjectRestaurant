from django.contrib.auth import get_user_model
from django.test import TestCase

from DjangoProjectRestaurant.review.models import Review

User = get_user_model()


class ReviewModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user',
            email='test@example.com',
            password='test_password',
        )
        self.review = Review.objects.create(
            user=self.user,
            content='This is a test review.',
        )

    def test_review_content(self):
        self.assertEqual(self.review.content, 'This is a test review.')


