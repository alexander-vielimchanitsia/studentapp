# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from studentapp.models import Student, Group
from forms import StudentForm, GroupForm
from django.template import RequestContext
from django.shortcuts import redirect
from django.http import HttpResponse


# Create your views here.


def index(request):
    table_student = Student.objects.all()
    table_group = Group.objects.all()
    return render_to_response('index.html', {
        'table_student': table_student,
        'table_group': table_group,
    })

def add_student(request):
    student_form = StudentForm()
    return render_to_response('add_student.html', {
        'student_form': student_form},
        context_instance=RequestContext(request)
    )

def add_group(request):
    group_form = GroupForm()
    return render(request, 'add_group.html', {
        'group_form': group_form})

def addstudent(request):
    student_form = StudentForm()
    errors = {}
    if request.POST.get('first_name', '').strip() == '':
        errors['first_name'] = 'Введіть будь ласка Ім’я студента'
    if request.POST.get('last_name', '').strip() == '':
        errors['last_name'] = 'Введіть будь ласка Прізвище студента'
    if request.POST.get('middle_name', '').strip() == '':
        errors['middle_name'] = 'Введіть будь ласка по батькові студента'
    if request.POST.get('date', '').strip() == '':
        errors['date'] = 'Введіть будь ласка дату народження студента'
    if request.POST.get('foto', '').strip() == '':
        errors['foto'] = 'Виберіть будь ласка фото студента'
    if request.POST.get('stud_bilet', '').strip() == '':
        errors['stud_bilet'] = 'Введіть будь ласка номер студентського білету'
    if request.POST.get('stud_group', '').strip() == '':
        errors['stud_group'] = 'Виберіть будь ласка групу студента'
    if errors:
        return render_to_response('add_student.html', {
            'errors': errors, 'student_form': student_form},
            context_instance=RequestContext(request)
        )
    else:
        return redirect('/')

        #if request.POST:
        #first_name = request.POST.get('first_name', '').strip() == ''
        #last_name = request.POST.get('last_name', '').strip() == ''
        #middle_name = request.POST.get('middle_name', '').strip() == ''
        #date = request.POST.get('date', '').strip() == ''
        #foto = request.POST.get('foto', '').strip() == ''
        #stud_bilet = request.POST.get('stud_bilet', '').strip() == ''
        #stud_group = request.POST.get('stud_group', '').strip() == ''

def addgroup(request):
    group_form = GroupForm(request.POST)
    if group_form.is_valid():
        group_form.save()
        return redirect('/')
    else:
        group_form = GroupForm()
    return render(request, 'add_group.html', { 'group_form': group_form })
        
    
