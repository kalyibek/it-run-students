from django.shortcuts import render, redirect
from . import models


def students_list(request):
    students = models.Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'www/students.html', context)


def student_detail(request, id):
    student = models.Student.objects.get(id=id)
    context = {
        'student': student
    }
    return render(request, 'www/student.html', context)


def student_create(request):
    if request.method == 'POST':
        klass = models.Klass.objects.get(id=request.POST['klass'])
        student = models.Student.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            age=request.POST['age'],
            characteristics=request.POST['characteristics'],
            photo=request.FILES['photo'],
            klass=klass
        )
        student.save()
        return redirect('/www/students')

    klasses = models.Klass.objects.all()
    context = {
        'klasses': klasses
    }
    return render(request, 'www/student_create.html', context)


def student_delete(request, id):
    student = models.Student.objects.get(id=id)
    student.delete()
    return redirect('/www/students')
