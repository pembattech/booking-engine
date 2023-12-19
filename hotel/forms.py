from django import forms

from .models import Hotel

class HotelForm(forms.ModelForm):
    
    class Meta:
        model = Hotel
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs = {'class': 'input-style'}),
            'address': forms.TextInput(attrs = {'class': 'input-style'}),
            'descrption': forms.TextInput(attrs = {'class': 'input-style'})
        }