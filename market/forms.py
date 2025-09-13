from django import forms
from .models import Bike, ContactMessage, Booking

class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = ['title','brand','model','variant','year','km_driven','owners','fuel_type','price','location','description','image']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name','email','phone','reason','message']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['bike','name','email','phone','amount']
        widgets = {
            'bike': forms.HiddenInput(),
            'amount': forms.HiddenInput(),
        }
