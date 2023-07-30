from django.test import TestCase, Client
from django.urls import reverse


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page(self):
        response = self.client.get(reverse('home page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/home-page.html')

    def test_about_page(self):
        response = self.client.get(reverse('about page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/about-page.html')

    def test_specials_page(self):
        response = self.client.get(reverse('specials page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/special-page.html')

    def test_events_page(self):
        response = self.client.get(reverse('events page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/events-page.html')

    def test_chefs_page(self):
        response = self.client.get(reverse('chefs page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/chefs-page.html')

    def test_gallery_page(self):
        response = self.client.get(reverse('gallery page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/gallery-page.html')
