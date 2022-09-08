from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.
def home(request):
    students = Student.objects.all()
    context = {
        "students": students 
    }
    return render(request, "fscohort/home.html", context)

def student_create(request):
    form = StudentForm()
    if request.method=='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student Created!')
            # form = StudentForm()
            return redirect("home")
    context = {
        "form": form,
    }
    return render(request, 'fscohort/student_create.html', context)

def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method=='POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            # form = StudentForm(instance=student)
            messages.success(request, 'Student Updated!')
            return redirect("home")
    context = {
        "form": form,
    }
    return render(request, 'fscohort/student_update.html', context)


def student_delete(request, id):
    # student = Student.objects.get(id=id)
    student = get_object_or_404(Student, id=id)
    if request.method=='POST':
            student.delete()
            return redirect("home")
    return render(request, 'fscohort/student_delete.html')


def student_detail(request, id):
    # student = Student.objects.get(id=id)
    student = get_object_or_404(Student, id=id)
    context = {
        'student': student,
    }
    return render(request, 'fscohort/student_detail.html', context)

