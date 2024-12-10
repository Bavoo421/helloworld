from django import forms
from .models import Patient
from .models import Appointment


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'mobile', 'gender', 'address']  # Include relevant fields

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'patient', 'date', 'time']  # Include relevant fields
