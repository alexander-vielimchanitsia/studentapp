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
    table_group = Group.objects.all()
    table_student = Student.objects.all()
    student_form = StudentForm()
    return render_to_response('add_student.html', {
        'student_form': student_form,
        'table_group': table_group,
        'table_student': table_student,},
        context_instance=RequestContext(request)
    )

def add_group(request):
    group_form = GroupForm()
    return render(request, 'add_group.html', {
        'group_form': group_form})

def addstudent(request):
    table_student = Student.objects.all()
    table_group = Group.objects.all()
    student_form = StudentForm()
    errors = {}
    error = {}
    if request.POST.get('first_name', '').strip() == '':
        errors['first_name'] = 'Введіть будь ласка ім’я студента'
        error['first_name'] = 'поле Ім’я обов’язвоке'
    if request.POST.get('last_name', '').strip() == '':
        errors['last_name'] = 'Введіть будь ласка прізвище студента'
        error['last_name'] = 'поле Прізвище обов’язкове'
    if request.POST.get('middle_name', '').strip() == '':
        errors['middle_name'] = 'Введіть будь ласка по батькові студента'
        error['middle_name'] = 'поле По батькові обов’язкове'
    if  request.POST.get('date', '').strip() == '':
        errors['date'] = 'Введіть будь ласка дату народження студента'
        error['date'] = 'поле Дата народження обов’язвове'
    if  request.FILES.get('foto', ''):
        errors['foto'] = 'Виберіть будь ласка фото студента'
        error['foto'] = 'поле Фото обов’язвове'
    if request.POST.get('stud_bilet', '').strip() == '':
        errors['stud_bilet'] = 'Введіть будь ласка ім’я студента'
        error['stud_bilet'] = 'поле No.студ-билета обов’язкове'
    if request.POST.get('stud_group', '').strip() == '':
        errors['stud_group'] = 'Виберіть будь ласка групу студента'
        error['stud_group'] = 'поле Група обов’язкове'
    if errors:
        return render_to_response('add_student.html', {
                                                        'errors': errors,
                                                        'error': error,
                                                        'table_student': table_student,
                                                        'student_form': student_form,
                                                        'table_group': table_group,
                                                        'first_name': request.POST.get('first_name')},
                                                        context_instance=RequestContext(request)
        )
    if not errors:
        return render_to_response('add_student.html', {
                                                        'table_student': table_student,
                                                        'student_form': student_form,
                                                        'table_group': table_group,},
                                                        context_instance=RequestContext(request)
        )
    else:
        Student.objects.all()
        s = Student(first_name = 'first_name',
                    last_name = 'last_name',
                    middle_name = 'middle_name',
                    date = 'date',
                    foto ='foto',
                    stud_bilet = 'stud_bilet',
                    stud_group = 'stud_group')
        s.save()
        return redirect('/')

def addgroup(request):
    group_form = GroupForm(request.POST)
    if group_form.is_valid():
        group_form.save()
        return redirect('/')
    else:
        group_form = GroupForm()
    return render(request, 'add_group.html', { 'group_form': group_form })
        
    
