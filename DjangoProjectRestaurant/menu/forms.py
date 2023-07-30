from django import forms
from django.contrib.auth import get_user_model
from DjangoProjectRestaurant.menu.models import MenuItem

UserModel = get_user_model()


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name != 'available':
                field.widget.attrs['class'] = 'form-control'

        self.fields['description'].widget.attrs['rows'] = 3
        self.fields['ingredients'].widget.attrs['rows'] = 3
