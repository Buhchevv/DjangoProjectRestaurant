from django.test import TestCase
from django.urls import reverse

from DjangoProjectRestaurant.contact.models import ContactMessage


class ContactTestCase(TestCase):

    def test_contact_page_post_valid_form(self):
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Test Subject',
            'message': 'Test Message'
        }
        response = self.client.post(reverse('contact page'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/contact-thank-you.html')

        self.assertEqual(ContactMessage.objects.count(), 1)
        contact_message = ContactMessage.objects.first()
        self.assertEqual(contact_message.name, 'John Doe')
        self.assertEqual(contact_message.email, 'john@example.com')
        self.assertEqual(contact_message.subject, 'Test Subject')
        self.assertEqual(contact_message.message, 'Test Message')


def test_contact_page_post_invalid_form(self):
    data = {
        'name': '',
        'email': '',
        'subject': '',
        'message': ''
    }
    response = self.client.post(reverse('contact page'), data)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'core/contact-page.html')
    self.assertFormError(response, 'form', 'name', 'This field is required.')
    self.assertFormError(response, 'form', 'email', 'This field is required.')
    self.assertFormError(response, 'form', 'subject', 'This field is required.')
    self.assertFormError(response, 'form', 'message', 'This field is required.')
