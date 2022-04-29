from django.db import models

# Create your models here.

class Student(models.Model):
    student_name = models.CharField( max_length=200)
    student_lname = models.CharField( max_length=200)
    email = models.CharField( max_length=200)
    phone = models.CharField( max_length=200)
    parent_name = models.CharField(max_length=200, null=True)
    parent_lname = models.CharField(max_length=200, null=True)
    parent_phone = models.CharField(max_length=50, null=True)
    year = models.IntegerField(null=True)



class Teacher(models.Model):
    teacher_name = models.CharField(max_length=200)
    teacher_lname = models.CharField(max_length=200)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    
class Subject(models.Model):
    subject_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.subject_name
    
    
        
class Parent(models.Model):
    parent_name = models.CharField(max_length=200)
    parent_lname = models.CharField(max_length=200)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=200, null=True)

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    grade = models.CharField(max_length=50)
    
class Archive(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=200)