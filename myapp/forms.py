
from django import forms

from myapp.models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        # fields = ['customer_name', 'customer_email', 'customer_phone', 'booking_date', 'booking_time', 'number_of_people', 'comments']
        fields = "__all__"


    