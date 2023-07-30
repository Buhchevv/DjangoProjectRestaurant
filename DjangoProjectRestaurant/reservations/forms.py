from django import forms

from DjangoProjectRestaurant.reservations.models import TableBooking


class TableBookingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['name'].initial = user.get_full_name()
            self.fields['email'].initial = user.email
            self.fields['phone'].initial = user.telephone_number

    class Meta:
        model = TableBooking
        fields = [
            'name',
            'email',
            'phone',
            'date',
            'time',
            'number_of_people',
            'message'
        ]

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Your name',
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Your email',
                    'class': 'form-control'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Phone number',
                    'class': 'form-control'
                }
            ),
            'date': forms.DateInput(
                attrs={
                    'placeholder': 'Date',
                    'class': 'form-control'
                }
            ),
            'time': forms.TimeInput(
                attrs={
                    'placeholder': 'Time',
                    'class': 'form-control'
                }
            ),
            'number_of_people': forms.NumberInput(
                attrs={
                    'placeholder': 'Number of people',
                    'class': 'form-control'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'placeholder': 'Message',

                    'class': 'form-control'
                }
            ),
        }