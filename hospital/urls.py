from django.urls import path
from .views import Home, About,Edit_Appointment,Edit_Patient,edit_doctor, Contact, Login, Logout_admin, Index,View_Doctor,Delete_Appointment,Add_Appointment,View_Appointment, Delete_Doctor, Add_Doctor, View_Patient,Delete_Patient,Add_Patient
from doctor.views import doctor_login, doctor_dashboard

urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('admin_login/', Login, name='admin_login'),
    path('logout/', Logout_admin, name='logout_admin'),
    path('index/', Index, name='dashboard'),
    path('view_doctor/', View_Doctor, name='view_doctor'),
    path('add_doctor/', Add_Doctor, name='add_doctor'),
    path('add_patient/', Add_Patient, name='add_patient'),
    path('delete_doctor(?p<int:pid>)/', Delete_Doctor, name='delete_doctor'),
    path('view_patient/', View_Patient, name='view_patient'),
    path('delete_patient(?p<int:pid>)/', Delete_Patient, name='delete_patient'),
    path('view_appointment/', View_Appointment, name='view_appointment'),
    path('add_appointment/', Add_Appointment, name='add_appointment'),
    path('delete_appointment(?p<int:pid>)/', Delete_Appointment, name='delete_appointment'),
    path('doctor_login/', doctor_login, name='doctor_login'),
    path('doctor_dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('edit-doctor/<int:pid>/', edit_doctor, name='edit_doctor'),
    path('edit-patient/<int:pid>/', Edit_Patient, name='edit_patient'),
    path('edit-appointment/<int:pid>/', Edit_Appointment, name='edit_appointment'),
]
