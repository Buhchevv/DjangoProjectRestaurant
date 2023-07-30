from django.views import generic as view, View
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from DjangoProjectRestaurant.contact.forms import ContactForm


class ContactView(View):
    def get(self, request):
        user = request.user if request.user.is_authenticated else None
        form = ContactForm(user=user)
        context = {
            'form': form,
        }
        return render(request, 'core/contact-page.html', context)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            subject = 'New Contact Message'
            message = f"A new message has been received:\n\nName: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nSubject: {form.cleaned_data['subject']}\nMessage: {form.cleaned_data['message']}"
            from_email = form.cleaned_data['email']
            to_email = [settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_email)

            user_subject = 'Thank You for Contacting Us'
            user_message = 'Thank you for contacting us. ' \
                           'We have received your message and will get back to you shortly.'
            send_mail(user_subject, user_message, settings.EMAIL_HOST_USER, [form.cleaned_data['email']])

            return render(request, 'core/contact-thank-you.html')

        context = {
            'form': form,
        }
        return render(request, 'core/contact-page.html', context)


class ContactSuccessView(view.TemplateView):
    template_name = 'core/contact-thank-you.html'
