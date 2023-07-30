from django import forms

from DjangoProjectRestaurant.contact.models import ContactMessage


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['name'].initial = user.get_full_name()
            self.fields['email'].initial = user.email

    class Meta:
        model = ContactMessage
        fields = [
            'name',
            'email',
            'subject',
            'message'
        ]
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your name'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your email'}
            ),
            'subject': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Subject'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your message'
                }
            ),
        }
