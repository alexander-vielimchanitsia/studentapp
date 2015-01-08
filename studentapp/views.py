# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from studentapp.models import Student, Group
from forms import StudentForm, GroupForm
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator

# Create your views here.


def index(request, page_number=1):
    table_student = Student.objects.all()
    student_page = Paginator(table_student, 10)
    return render_to_response('index.html',
        {'table_student': student_page.page(page_number),
        'a': 2},
        context_instance=RequestContext(request)
    )

def groups(request, page_number=1):
    table_group = Group.objects.all()
    group_page = Paginator(table_group, 10)
    return render_to_response('groups.html',
        {'table_group': group_page.page(page_number)},
        context_instance=RequestContext(request)
    )

def add_student(request):
    table_student = Student.objects.all()
    table_group = Group.objects.all()
    student_form = StudentForm()
    files = request.FILES
    data = request.POST
    errors = {}
    error = {}
    if data.get('first_name', '').strip() == '':
        errors['first_name'] = 'Введіть будь ласка ім’я студента'
        error['first_name'] = 'поле Ім’я обов’язкоке'
    if data.get('last_name', '').strip() == '':
        errors['last_name'] = 'Введіть будь ласка прізвище студента'
        error['last_name'] = 'поле Прізвище обов’язкове'
    if data.get('middle_name', '').strip() == '':
        errors['middle_name'] = 'Введіть будь ласка по батькові студента'
        error['middle_name'] = 'поле По батькові обов’язкове'
    if data.get('date', '').strip() == '':
        errors['date'] = 'Введіть будь ласка дату народження студента'
        error['date'] = 'поле Дата народження обов’язкове'
    if not files.get('foto', None) or files['foto'].size == 0:
        errors['foto'] = 'Виберіть будь ласка фото студента'
        error['foto'] = 'поле Фото обов’язкове'
    if data.get('stud_bilet', '').strip() == '':
        errors['stud_bilet'] = 'Введіть будь ласка номер студ.білету студента'
        error['stud_bilet'] = 'поле No.студ-билета обов’язкове'
    if data.get('stud_group', '').strip() == '':
        errors['stud_group'] = 'Виберіть будь ласка групу студента'
        error['stud_group'] = 'поле Група обов’язкове'
    if data.get('submit'):
        if errors:
            return render_to_response('add_student.html',
                {'errors': errors,
                'error': error,
                'table_group': table_group},
                context_instance=RequestContext(request)
            )
        else:
            s = Student(first_name = data['first_name'],
                        last_name = data['last_name'],
                        middle_name = data['middle_name'],
                        date = data['date'],
                        foto = files['foto'],
                        stud_bilet = data['stud_bilet'],
                        stud_group = Group.objects.get(
                            pk=data['stud_group']
                            )
                        )
            s.save()
            return redirect(
                u'/index/?status_message=Студент успішно доданий!'
                )
    return render_to_response('add_student.html',
        {'table_student': table_student,
        'table_group': table_group,
        'student_form': student_form,
        'groups': groups},
        context_instance=RequestContext(request)
    )
def add_group(request):
    table_student = Student.objects.all()
    data = request.POST
    errors = {}
    error = {}
    if data.get('name_group', '').strip() == '':
        errors['name_group'] = 'Введіть будь ласка назву групи'
        error['name_group'] = 'поле Назва групи обов’язкове'
    if data.get('submit'):
        if errors:
            return render_to_response('add_group.html',
                {'errors': errors,
                'error': error,
                'table_student': table_student},
                context_instance=RequestContext(request)
            )
        else:
            if data.get('king_group', '').strip() == '':
                g = Group(
                    name_group = request.POST['name_group'],
                    king_group = None
                )
            else:
                g = Group(
                    name_group = request.POST['name_group'],
                    king_group = Student.objects.get(
                        pk=data['king_group']
                        )
                )
            g.save()
            return redirect(
                u'/groups/?status_message=Група успішно додана!'
                )
    return render_to_response('add_group.html',
        {'table_student': table_student},
        context_instance=RequestContext(request)
    )
def edit_student(request, student_id):
    table_student = Student.objects.get(id=student_id)
    student_form = StudentForm()
    files = request.FILES
    data = request.POST
    errors = {}
    error = {}
    if data.get('first_name', '').strip() == '':
        errors['first_name'] = 'Введіть будь ласка ім’я студента'
        error['first_name'] = 'поле Ім’я обов’язкоке'
    if data.get('last_name', '').strip() == '':
        errors['last_name'] = 'Введіть будь ласка прізвище студента'
        error['last_name'] = 'поле Прізвище обов’язкове'
    if data.get('middle_name', '').strip() == '':
        errors['middle_name'] = 'Введіть будь ласка по батькові студента'
        error['middle_name'] = 'поле По батькові обов’язкове'
    if data.get('date', '').strip() == '':
        errors['date'] = 'Введіть будь ласка дату народження студента'
        error['date'] = 'поле Дата народження обов’язкове'
    if files.get('new_foto') > 0:
        if not files.get('new_foto', None) or files['new_foto'].size == 0:
            errors['foto'] = 'Виберіть будь ласка фото студента'
            error['foto'] = 'поле Фото обов’язкове'
    if data.get('stud_bilet', '').strip() == '':
        errors['stud_bilet'] = 'Введіть будь ласка студ.білет студента'
        error['stud_bilet'] = 'поле No.студ-билета обов’язкове'
    if data.get('stud_group', '').strip() == '':
         errors['stud_group'] = 'Виберіть будь ласка групу студента'
         error['stud_group'] = 'поле Група обов’язкове'
    if data.get('submit'):
        if errors:
            return render_to_response('edit_student.html',
                {'errors': errors,
                'error': error,
                'table_student': table_student,
                'table_group': Group.objects.all(),
                'student_form': student_form},
                context_instance=RequestContext(request)
            )
        else:
            if files.get('new_foto') > 0:
                student_object = Student(
                    id=student_id,
                    first_name = data['first_name'],
                    last_name = data['last_name'],
                    middle_name = data['middle_name'],
                    date = data['date'],
                    foto = files['new_foto'],
                    stud_bilet = data['stud_bilet'],
                    stud_group = Group(pk=data['stud_group'])
                )
            else:
                student_object = Student(
                    id=student_id,
                    first_name = data['first_name'],
                    last_name = data['last_name'],
                    middle_name = data['middle_name'],
                    date = data['date'],
                    foto = table_student.foto,
                    stud_bilet = data['stud_bilet'],
                    stud_group = Group(pk=data['stud_group'])
                )
            student_object.save()
            return redirect(
                u'/index/?status_message=Студент успішно відредагований!'
                )

    return render_to_response('edit_student.html',
        {'table_student': table_student,
        'table_group': Group.objects.all(),
        'groups': groups},
        context_instance=RequestContext(request)
    )

def edit_group(request, group_id):
    table_group = Group.objects.get(id=group_id)
    table_student = Student.objects.all()
    data = request.POST
    errors = {}
    error = {}
    if data.get('name_group', '').strip() == '':
        errors['name_group'] = 'Введіть будь ласка назву групи'
        error['name_group'] = 'поле Назва групи обов’язкове'
    if data.get('submit'):
        if errors:
            return render_to_response('edit_group.html',
                {'errors': errors,
                'error': error,
                'table_student': table_student,
                'table_group': table_group},
                context_instance=RequestContext(request)
            )
        else:
            if data.get('king_group', '').strip() == '':
                group_object = Group(
                    id = group_id,
                    name_group = data['name_group'],
                    king_group = None
                )
            else:
                group_object = Group(
                    id = group_id,
                    name_group = data['name_group'],
                    king_group = Student(pk=data['king_group'])
                )
            group_object.save()
            return redirect(
                u'/groups/?status_message=Група успішно відредагована!'
                )
    return render_to_response('edit_group.html',
        {'table_student': table_student,
        'table_group': table_group},
        context_instance=RequestContext(request)
    )

def stud_delete(request, student_id):
    s = Student.objects.get(id=student_id)
    s.delete()
    return redirect(
                u'/index/?status_message=Студент успішно видалений!'
                )

def group_delete(request, group_id):
    g = Group.objects.get(id=group_id)
    g.delete()
    return redirect(
                u'/groups/?status_message=Група успішно видалена!'
                )
