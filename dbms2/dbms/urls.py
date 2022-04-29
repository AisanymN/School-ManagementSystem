from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name = 'index'),
path('add/', views.adding,name = 'adding'),
path('students/', views.students, name = 'students'),
path('parents/', views.parents, name = 'parents'),
path('teachers/', views.teachers, name = 'teachers'),
path('subjects/', views.subjects, name = 'subjects'),
path('grades/', views.grade, name = 'grades'),
path('add_teacher/', views.add_teacher, name='add_teacher')
]   