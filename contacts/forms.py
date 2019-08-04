from django import forms
from .models import people


class contactform(forms.ModelForm):
    class Meta:
        model = people
        fields = [
            "name",
            "phone",
            "email"
        ]
