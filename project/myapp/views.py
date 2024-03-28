from django.http import HttpResponseRedirect
from django.shortcuts import render
from  django.urls import reverse

from .models import Student
from .forms import StudentForm

# Create your views here.
def index(request):
    return render(request, "index.html", {
        'students': Student.objects.all()
    })

def view_student(request, id):
    return HttpResponseRedirect(reverse('index'))

def add(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      new_student_usn = form.cleaned_data['student_usn']
      new_first_name = form.cleaned_data['first_name']
      new_last_name = form.cleaned_data['last_name']
      new_email = form.cleaned_data['email']
      new_student_course = form.cleaned_data['student_course']

      new_student = Student(
        student_usn=new_student_usn,
        first_name=new_first_name,
        last_name=new_last_name,
        email=new_email,
        student_course=new_student_course,
      )
      new_student.save()
      return render(request, 'add.html', {
        'form': StudentForm(),
        'success': True
      })
  else:
    form = StudentForm()
  return render(request, 'add.html', {
    'form': StudentForm()
  })

def edit(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Student.objects.get(pk=id)
    form = StudentForm(instance=student)
  return render(request, 'edit.html', {
    'form': form
  })