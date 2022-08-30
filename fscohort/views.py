from multiprocessing import context
from django.shortcuts import render, redirect
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
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        "form" : form
    }

    return render(request, 'fscohort/student_add.html', context)


def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance = student)
    if request.method=='POST':
        form=StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        'form' : form
    }
    return render(request, 'fscohort/student_update.html', context)

def student_delete(request, id):
    student = Student.objects.get(id=id)
    if request.method=='POST':
        student.delete()
        return redirect('list')
    context = {
        'student' : student
    }

    return render(request, 'fscohort/student_delete.html', context)