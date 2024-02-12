from django.urls import path
from . import views


urlpatterns = [
    path('students/', views.students_list, name='student_list'),
    path('students/<int:id>', views.student_detail, name='student_detail'),
    path('students/create', views.student_create, name='student_create'),
    path('students/delete/<int:id>', views.student_delete, name='student_delete'),
]
