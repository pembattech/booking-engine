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
            'description': forms.Textarea(attrs={'class': 'input-style'}),
            'price': forms.TextInput(attrs={'class': 'input-style'}),
        }
        
from django import forms
from .models import Hotel, HotelImage

class EditHotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'address', 'description', 'price']

    images = MultipleFileField(required=False)
    images_to_delete = forms.MultipleChoiceField(choices=[], widget=forms.CheckboxSelectMultiple, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:  # If editing an existing hotel
            self.fields['images_to_delete'].choices = [
                (image.id, f"{image.image.name} ({image.image.url})") for image in self.instance.images.all()
            ]

    def save(self, commit=True):
        hotel = super().save(commit=False)

        # Handle image uploads
        for image in self.cleaned_data['images']:
            hotel_image = HotelImage.objects.create(image=image)
            hotel.images.add(hotel_image)

        # Handle image deletions
        for image_id in self.cleaned_data['images_to_delete']:
            hotel_image = HotelImage.objects.get(id=image_id)
            hotel.images.remove(hotel_image)
            hotel_image.delete()

        if commit:
            hotel.save()
        return hotel
