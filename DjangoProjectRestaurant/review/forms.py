from DjangoProjectRestaurant.review.models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content']
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'placeholder': 'Your Review',
                }
            ),
        }