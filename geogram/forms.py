from django import forms
from .models import PinDrop

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime'

class newPinForm(forms.ModelForm):

    longitude = forms.DecimalField(max_digits=10,decimal_places=6,max_value=180,min_value=-180)
    latitude = forms.DecimalField(max_digits=10,decimal_places=6,max_value=90,min_value=-90)
    pinimage = forms.ImageField()

    class Meta:
        model = PinDrop
        fields = ('pinimage','longitude','latitude','pinbody',)
