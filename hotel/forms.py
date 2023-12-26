from django import forms
from datetime import *

from .models import Hotel, HotelImage, Reservation


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ["name", "address", "description", "price"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "input-style"}),
            "address": forms.TextInput(attrs={"class": "input-style"}),
            "description": forms.Textarea(attrs={"class": "input-style"}),
            "price": forms.TextInput(attrs={"class": "input-style"}),
        }


class HotelImageForm(forms.ModelForm):
    class Meta:
        model = HotelImage
        fields = ["hotel", "hotel_images"]


HotelImageFormSet = forms.inlineformset_factory(
    Hotel, HotelImage, form=HotelImageForm, extra=1, can_delete=True
)

# forms.py
from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['check_in_date', 'check_out_date']
        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)

        # Set default values for check-in and check-out dates
        today = date.today()
        tomorrow = today + timedelta(days=1)

        self.fields['check_in_date'].initial = today
        self.fields['check_out_date'].initial = tomorrow
        
    def clean(self):
        cleaned_data = super().clean()
        check_in_date = cleaned_data.get('check_in_date')
        check_out_date = cleaned_data.get('check_out_date')

        if check_in_date and check_out_date and check_out_date <= check_in_date:
            raise forms.ValidationError("Check-out date must be after the check-in date")

        return cleaned_data
