from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_usn', 'first_name', 'last_name', 'email', 'student_course']
        labels = {
            'student_usn': 'Student Usn',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'student_course': 'Student Course',
        }
        widgets={
            'student_usn': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'student_course': forms.TextInput(attrs={'class': 'form-control'}),
        }