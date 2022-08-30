from multiprocessing import context
from django.shortcuts import render
from .models import Student
from .forms import StudentForm

# Create your views here.

def index(request):
    return render(request, 'fscohort/index.html')

def student_list(request): 
    students = Student.objects.all()
    context = {
        "students" : students
    }
    return render(request, 'fscohort/student_list.html', context)

def student_add(request):
    form = StudentForm()
    context = {
        "form" : form
    }

    return render(request, 'fscohort/student_add.html', context)