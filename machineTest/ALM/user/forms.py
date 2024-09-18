from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Flight

# Admin Registration Form
class AdminRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

from django import forms
from django.contrib.auth.forms import AuthenticationForm

# Admin Login Form
class AdminLoginForm(AuthenticationForm):
    pass

from django import forms
from .models import Flight

# Flight Form
class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['flight_id', 'dep_airport', 'dep_date', 'dep_time', 'arr_airport', 'arr_date', 'arr_time']

    def clean_flight_id(self):
        flight_id = self.cleaned_data.get('flight_id')
        if Flight.objects.filter(flight_id=flight_id).exists():
            raise forms.ValidationError('Flight with this ID already exists.')
        return flight_id
