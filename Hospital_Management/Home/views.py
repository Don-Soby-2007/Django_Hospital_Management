from django.shortcuts import render
from .models import Departments, Doctors

# Create your views here.


def index(request):
    datas = {
        'nums': [1, 2, 3, 4, 5, 6, 7, 8, 9]
    }

    return render(request, 'index.html', datas)


def about(request):
    return render(request, 'about.html')


def booking(request):
    return render(request, 'booking.html')


def doctors(request):
    dict_doctors = {
        "doctors": Doctors.objects.all()
    }
    return render(request, 'doctors.html', dict_doctors)


def contact(request):
    return render(request, 'contact.html')


def department(request):
    dict_dept = {
        "dept": Departments.objects.all()
    }
    return render(request, 'department.html', dict_dept)
