from django.urls import path
from . import views

urlpatterns=[
    path("", views.home, name='home'),
    path("index/", views.index, name="index"),
    path('<int:id>', views.view_student, name='view_student'),
    path("add/", views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register')
]