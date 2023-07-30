from django.test import TestCase

from DjangoProjectRestaurant.subscribers.models import Subscriber


class SubscriberModelTest(TestCase):

    def setUp(self):
        self.subscriber = Subscriber.objects.create(
            email='test@example.com',
        )

    def test_subscriber_content(self):
        self.assertEqual(str(self.subscriber), 'test@example.com')
        self.assertEqual(self.subscriber.email, 'test@example.com')
        self.assertIsNotNone(self.subscriber.date_subscribed)
