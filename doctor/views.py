from django.contrib.auth.hashers import check_password
from django.shortcuts import redirect, render

from doctor.models import Doctor
from hospital.models import Appointment


def doctor_login(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")

        try:
            doctor = Doctor.objects.get(name=name)
            # Check if the provided password matches the stored hash
            if check_password(password, doctor.password):
                request.session["doctor_id"] = doctor.id  # Store doctor ID in session
                return redirect("doctor_dashboard")  # Redirect to the doctor dashboard
            else:
                return render(request, "hospital/templates/doctor_login.html", {"error": "Invalid credentials"})
        except Doctor.DoesNotExist:
            return render(request, "doctor_login.html", {"error": "Doctor not found"})

    return render(request, "doctor_login.html")


def doctor_dashboard(request):
    doctor_id = request.session.get("doctor_id")
    if not doctor_id:
        return redirect("doctor_login")  # Redirect to login if not logged in

    appointments = Appointment.objects.filter(doctor_id=doctor_id)
    return render(request, "doctor_dashboard.html", {"appointments": appointments})

