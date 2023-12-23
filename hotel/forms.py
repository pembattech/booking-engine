from django import forms
from django.forms.widgets import ClearableFileInput

from .models import Hotel


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class HotelForm(forms.ModelForm):
    images = MultipleFileField()

    class Meta:
        model = Hotel
        fields = ['name', 'address', 'description', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-style'}),
            'address': forms.TextInput(attrs={'class': 'input-style'}),
            'description': forms.TextInput(attrs={'class': 'input-style'}),
            'price': forms.TextInput(attrs={'class': 'input-style'}),
        }
