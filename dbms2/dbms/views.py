from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
import datetime
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request, 'main.html')

def adding(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adding')
    else:
        form = StudentForm()
    return render(request, 'add.html',  {'form': form})


def students(request):
    object_list = Student.objects.all()
    student_list = Student.objects.all()
    
    search_query = request.POST.get('search')
    
    if not search_query:
        search_query = ""
    if request.method == 'POST':
        object_list = Student.objects.filter(student_name__icontains = search_query)
   
    return render(request, 'students.html', {'object_list': object_list})

def current_year():
    return datetime.date.today().year

def parents(request):
    parents_list = Parent.objects.all()
    return render(request, 'parents.html', {'parents_list': parents_list})

def teachers(request):
    teachers_list = Teacher.objects.all()
    return render (request, 'teachers.html',{'teachers_list': teachers_list} )

def subjects(request):
    subject_list = Subject.objects.all()
    return render(request, 'subjects.html', {'subject_list': subject_list})

def grade(request):
    grades_list = Grade.objects.all()
    return render(request, 'grades.html', {'grades_list': grades_list})


def add_teacher(request):
    
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_teacher')
    else:
        form = TeacherForm()
    return render(request, 'add_teacher.html',  {'form': form}) 