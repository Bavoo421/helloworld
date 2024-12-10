
from django.urls import path
from .views import doctor_login, doctor_dashboard

urlpatterns = [
    path('doctor_login/', doctor_login, name='doctor_login'),
    path('doctor_dashboard/', doctor_dashboard, name='doctor_dashboard'),
]
