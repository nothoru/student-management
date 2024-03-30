from django.db import models

# Create your models here.
class Student(models.Model):
    student_usn = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    student_course = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}"
    