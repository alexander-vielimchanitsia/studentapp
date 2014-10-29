# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from studentapp.models import Student, Group
from forms import StudentForm, GroupForm
from django.template import RequestContext
from django.http import HttpResponse
from django.core.paginator import Paginator

# Create your views here.


def index(request, page_number = 1):
    table_student = Student.objects.all()
    student_page = Paginator(table_student, 10)
    return render_to_response('index.html', {
        'table_student': student_page.page(page_number),
    })

def groups(request, page_number = 1):
    table_group = Group.objects.all()
    group_page = Paginator(table_group, 10)
    return render_to_response('groups.html', {
        'table_group': group_page.page(page_number)
    })

def addstudent(request):
    table_student = Student.objects.all()
    table_group = Group.objects.all()
    student_form = StudentForm()
    errors = {}
    error = {}
    if request.POST.get('first_name', '').strip() == '':
        errors['first_name'] = 'Введіть будь ласка ім’я студента'
        error['first_name'] = 'поле Ім’я обов’язкоке'
    if request.POST.get('last_name', '').strip() == '':
        errors['last_name'] = 'Введіть будь ласка прізвище студента'
        error['last_name'] = 'поле Прізвище обов’язкове'
    if request.POST.get('middle_name', '').strip() == '':
        errors['middle_name'] = 'Введіть будь ласка по батькові студента'
        error['middle_name'] = 'поле По батькові обов’язкове'
    if request.POST.get('date', '').strip() == '':
        errors['date'] = 'Введіть будь ласка дату народження студента'
        error['date'] = 'поле Дата народження обов’язкове'
    if not request.FILES.get('foto', None) or request.FILES['foto'].size == 0:
        errors['foto'] = 'Виберіть будь ласка фото студента'
        error['foto'] = 'поле Фото обов’язкове'
    if request.POST.get('stud_bilet', '').strip() == '':
        errors['stud_bilet'] = 'Введіть будь ласка ім’я студента'
        error['stud_bilet'] = 'поле No.студ-билета обов’язкове'
    if request.POST.get('stud_group', '').strip() == '':
        errors['stud_group'] = 'Виберіть будь ласка групу студента'
        error['stud_group'] = 'поле Група обов’язкове'
    if request.POST.get('submit'):
        if not errors:
            s = Student(first_name = request.POST['first_name'],
                        last_name = request.POST['last_name'],
                        middle_name = request.POST['middle_name'],
                        date = request.POST['date'],
                        foto = request.FILES['foto'],
                        stud_bilet = request.POST['stud_bilet'],
                        stud_group = Group.objects.get(pk=request.POST['stud_group'])
            )
            s.save()
            return redirect('/')
        if errors:
            return render_to_response('add_student.html', {
                                                            'errors': errors,
                                                            'error': error,
                                                            'table_student': table_student,
                                                            'table_group': table_group,
                                                            'student_form': student_form,},
                                                            context_instance=RequestContext(request)
            )
    return render_to_response('add_student.html', {
                                                    'table_student': table_student,
                                                    'table_group': table_group,
                                                    'student_form': student_form,
                                                    'groups': groups},
                                                    context_instance=RequestContext(request)
    )
def addgroup(request):
    table_student = Student.objects.all()
    group_form = GroupForm(request.POST)
    errors = {}
    error = {}
    if request.POST.get('name_group', '').strip() == '':
        errors['name_group'] = 'Введіть будь ласка назву групи'
        error['name_group'] = 'поле Назва групи обов’язкове'
    if request.POST.get('submit'):
        if errors:
            return render_to_response('add_group.html', {
                                                        'errors': errors,
                                                        'error': error,
                                                        'group_form': group_form,
                                                        'table_student': table_student},
                                                        context_instance=RequestContext(request)
            )
        if not errors:
            import pdb;pdb.set_trace()
            g = Group(name_group = request.POST['name_group'],
                    king_group = Student.objects.get(pk=request.POST['king_group'])
            )
            g.save()
            return redirect('/groups/')
    return render_to_response('add_group.html', {
                                                'group_form': group_form,
                                                'table_student': table_student},
                                                context_instance=RequestContext(request)
    )
def edit_student(request, student_id):
    table_student = Student.objects.get(id=student_id)
    student_form = StudentForm()
    errors = {}
    error = {}
    if request.POST.get('first_name', '').strip() == '':
        errors['first_name'] = 'Введіть будь ласка ім’я студента'
        error['first_name'] = 'поле Ім’я обов’язкоке'
    if request.POST.get('last_name', '').strip() == '':
        errors['last_name'] = 'Введіть будь ласка прізвище студента'
        error['last_name'] = 'поле Прізвище обов’язкове'
    if request.POST.get('middle_name', '').strip() == '':
        errors['middle_name'] = 'Введіть будь ласка по батькові студента'
        error['middle_name'] = 'поле По батькові обов’язкове'
    if request.POST.get('date', '').strip() == '':
        errors['date'] = 'Введіть будь ласка дату народження студента'
        error['date'] = 'поле Дата народження обов’язкове'
    if not request.FILES.get('foto', None) or request.FILES['foto'].size == 0:
        errors['foto'] = 'Виберіть будь ласка фото студента'
        error['foto'] = 'поле Фото обов’язкове'
    if request.POST.get('stud_bilet', '').strip() == '':
        errors['stud_bilet'] = 'Введіть будь ласка ім’я студента'
        error['stud_bilet'] = 'поле No.студ-билета обов’язкове'
    if request.POST.get('stud_group', '').strip() == '':
        errors['stud_group'] = 'Виберіть будь ласка групу студента'
        error['stud_group'] = 'поле Група обов’язкове'
    if request.POST.get('submit'):
        if not errors:
            object = Student.objects.get(id=student_id,
                                         first_name = request.POST['first_name'],
                                         last_name = request.POST['last_name'],
                                         middle_name = request.POST['middle_name'],
                                         date = request.POST['date'],
                                         foto = request.FILES['foto'],
                                         stud_bilet = request.POST['stud_bilet'],
                                         stud_group = Group.objects.get(pk=request.POST['stud_group'])
            )
            # model = Student(request.POST)
            #  s = Student(first_name = request.POST['first_name'],
            #              last_name = request.POST['last_name'],
            #              middle_name = request.POST['middle_name'],
            #              date = request.POST['date'],
            #              foto = request.FILES['foto'],
            #              stud_bilet = request.POST['stud_bilet'],
            #              stud_group = Group.objects.get(pk=request.POST['stud_group'])
            # )
            # estud = model.save(commit=False)
            # estud.s = table_student
            object.save()
            return redirect('/')
        if errors:
            return render_to_response('edit_student.html', {
                                                            'errors': errors,
                                                            'error': error,
                                                            'table_student': table_student,
                                                            'table_group': Group.objects.all(),
                                                            'student_form': student_form,},
                                                            context_instance=RequestContext(request)
            )
    return render_to_response('edit_student.html', {
                                                    'table_student': table_student,
                                                    'table_group': Group.objects.all(),
                                                    'groups': groups},
                                                    context_instance=RequestContext(request)
    )

def stud_delete(request, student_id):
    s = Student.objects.get(id=student_id)
    s.delete()
    return redirect('/')

def group_delete(request, group_id):
    g = Group.objects.get(id=group_id)
    g.delete()
    return redirect('/groups/')