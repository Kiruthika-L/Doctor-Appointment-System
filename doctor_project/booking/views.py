from django.shortcuts import render, redirect
from .models import Doctor, Patient, Appointment


def home(request):
    appointments = Appointment.objects.all()
    return render(request, "bookings/home.html", {"appointments": appointments})


def book_appointment(request):
    if request.method == "POST":
        patient_name = request.POST.get("patient_name")
        doctor_id = request.POST.get("doctor")
        date = request.POST.get("date")
        time = request.POST.get("time")

        patient = Patient.objects.create(
            name=patient_name
        )

        doctor = Doctor.objects.get(id=doctor_id)

        Appointment.objects.create(
            patient=patient,
            doctor=doctor,
            date=date,
            time=time
        )

        return redirect("home")

    doctors = Doctor.objects.all()
    return render(request, "bookings/appointment_form.html", {"doctors": doctors})