from DjangoProjectRestaurant.subscribers.models import Subscriber
from django import forms


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
