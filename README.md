# Student Management System
## Purpose and Description
The purpose of the Student Management System is to provide an efficient platform for managing student data within an educational institution. It enables administrators and teachers to maintain accurate records of student information, courses enrolled, and academic performance. Additionally, it facilitates communication between stakeholders and streamlines administrative tasks related to student management.

## Install Django if not installed
    py -m pip install Django

## Explore
Try it out by installing the requirements. (Works only with python >= 3.8, due to Django 4)

    pip install -r requirements.txt

Migrate:

    python manage.py migrate

And then start the server (default: http://localhost:8000)

    python manage.py runserver


Now you can browse the [API](http://localhost:8000/api/)


[license-url]: https://github.com/rtzll/django-todolist/blob/master/LICENSE
[license-image]: https://img.shields.io/badge/license-MIT-blue.svg?style=flat

[travis-url]: https://travis-ci.org/rtzll/django-todolist
[travis-image]: https://travis-ci.org/rtzll/django-todolist.svg?branch=master
