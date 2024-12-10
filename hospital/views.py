from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from doctor.models import Doctor
from .forms import PatientForm
from .models import Patient
from .models import Appointment
from django.contrib.auth.hashers import make_password
from doctor.forms import DoctorForm
from .forms import AppointmentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password

def About(request):
    return render(request, 'about.html')

def Home(request):
    return render(request, 'home.html')

def Contact(request):
    return render(request, 'contact.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    appointments = Appointment.objects.all()
    d = 0
    p = 0
    a = 0
    for i in doctors:
        d+=1
    for i in patients:
        p+=1
    for i in appointments:
        a+=1
    d1 = {'d':d, 'p':p, 'a':a}
    return render(request, 'index.html', d1)

def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"

            else:
                error = "yes"

        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    logout(request)
    return redirect('admin_login')

def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc': doc}
    return render(request, 'view_doctor.html', d)

def Delete_Doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')

def Add_Doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        m = request.POST['mobile']
        sp = request.POST['specialization']
        pw = request.POST['password']  # Retrieve password from the form
        try:
            # Hash the password before saving it
            hashed_password = make_password(pw)
            Doctor.objects.create(name=n, mobile=m, specialization=sp, password=hashed_password)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_doctor.html', d)


def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Patient.objects.all()
    d = {'doc': doc}
    return render(request, 'view_patient.html', d)

def Delete_Patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')

def Add_Patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        m = request.POST['mobile']
        g = request.POST['gender']
        a = request.POST['address']
        try:
            Patient.objects.create(name=n, mobile=m, gender=g, address=a)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_patient.html', d)


def Add_Appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()

    if request.method == 'POST':
        # Log received POST data
        print("POST data:", request.POST)

        n = request.POST.get('doctor')  # Get doctor name from POST
        p = request.POST.get('patient')  # Get patient name from POST
        d = request.POST.get('date')  # Get date from POST
        t = request.POST.get('time')  # Get time from POST

        # Log the individual variables
        print(f"Doctor: {n}, Patient: {p}, Date: {d}, Time: {t}")

        # Retrieve doctor and patient objects
        doctor = Doctor.objects.filter(name=n).first()
        patient = Patient.objects.filter(name=p).first()

        # Log the retrieved objects
        print(f"Retrieved Doctor: {doctor}, Retrieved Patient: {patient}")

        if not doctor or not patient:
            error = "yes"
            print("Error: Doctor or Patient not found.")
        else:
            try:
                # Create the appointment
                Appointment.objects.create(doctor=doctor, patient=patient, date=d, time=t)
                error = "no"
            except Exception as e:
                print("Error creating appointment:", e)  # Log the exact error
                error = "yes"

    # Pass data to the template
    context = {'doc': doctor1, 'patient': patient1, 'error': error}
    return render(request, 'add_appointment.html', context)

def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Appointment.objects.all()
    d = {'doc': doc}
    return render(request, 'view_appointment.html', d)

def Delete_Appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    app = Appointment.objects.get(id=pid)
    app.delete()
    return redirect('view_appointment')

from django.contrib import messages

@login_required
def edit_doctor(request, pid):
    if not request.user.is_staff:
        return redirect('login')

    doctor = get_object_or_404(Doctor, id=pid)

    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, "Changes saved successfully!")
            return redirect('view_doctor')
    else:
        form = DoctorForm(instance=doctor)

    return render(request, 'edit_doctor.html', {'form': form, 'doctor': doctor})

def Edit_Patient(request, pid):
    if not request.user.is_staff:
        return redirect('login')

    patient = get_object_or_404(Patient, id=pid)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, "Patient details updated successfully!")
            return redirect('view_patient')
    else:
        form = PatientForm(instance=patient)

    return render(request, 'edit_patient.html', {'form': form, 'patient': patient})

def Edit_Appointment(request, pid):
    if not request.user.is_staff:
        return redirect('login')

    appointment = get_object_or_404(Appointment, id=pid)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, "Appointment details updated successfully!")
            return redirect('view_appointment')
    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'edit_appointment.html', {'form': form, 'appointment': appointment})





# Create your views here.
# Create your views here.
