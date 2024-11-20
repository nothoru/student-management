from django.db import models

from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    student_usn = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    student_course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, related_name="students")

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}"
