# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from studentapp.models import Student, Group
from forms import StudentForm, GroupForm
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator

# Create your views here.

def test(request):
    return render_to_response('test.html')

def index(request, page_number = 1):
    table_student = Student.objects.all()
    student_page = Paginator(table_student, 10)
    return render_to_response('index.html', {
        'table_student': student_page.page(page_number),
    },
    context_instance=RequestContext(request)
    )

def groups(request, page_number = 1):
    table_group = Group.objects.all()
    group_page = Paginator(table_group, 10)
    return render_to_response('groups.html', {
        'table_group': group_page.page(page_number)
    },
    context_instance=RequestContext(request)
    )

def addstudent(request):
    table_student = Student.objects.all()
    table_group = Group.objects.all()
    if request.POST:
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(u'/index/?status_message=Студент успішно доданий!/')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {
                                                'table_group': table_group,
                                                'form': form,
                                                })
    
def addgroup(request):
    table_student = Student.objects.all()
    if request.POST:
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(u'/groups/?status_message=Група успішно додана!/')
    else:
        form = GroupForm()
    return render(request, 'add_group.html', {
                                                'table_student': table_student,
                                                'form': form,
                                                })

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
    if request.FILES.get('new_foto') > 0:
        if not request.FILES.get('new_foto', None) or request.FILES['new_foto'].size == 0:
            errors['foto'] = 'Виберіть будь ласка фото студента'
            error['foto'] = 'поле Фото обов’язкове'
    if request.POST.get('stud_bilet', '').strip() == '':
        errors['stud_bilet'] = 'Введіть будь ласка ім’я студента'
        error['stud_bilet'] = 'поле No.студ-билета обов’язкове'
    if request.POST.get('stud_group', '').strip() == '':
         errors['stud_group'] = 'Виберіть будь ласка групу студента'
         error['stud_group'] = 'поле Група обов’язкове'
    if request.POST.get('submit'):
        if errors:
            return render_to_response('edit_student.html', {
                                                            'errors': errors,
                                                            'error': error,
                                                            'table_student': table_student,
                                                            'table_group': Group.objects.all(),
                                                            'student_form': student_form,},
                                                            context_instance=RequestContext(request)
            )

        else:
            if request.FILES.get('new_foto') > 0:
                student_object = Student(id=student_id,
                                        first_name = request.POST['first_name'],
                                        last_name = request.POST['last_name'],
                                        middle_name = request.POST['middle_name'],
                                        date = request.POST['date'],
                                        foto = request.FILES['new_foto'],
                                        stud_bilet = request.POST['stud_bilet'],
                                        stud_group = Group(pk=request.POST['stud_group'])
                )
            else:
                student_object = Student(id=student_id,
                                        first_name = request.POST['first_name'],
                                        last_name = request.POST['last_name'],
                                        middle_name = request.POST['middle_name'],
                                        date = request.POST['date'],
                                        foto = table_student.foto,
                                        stud_bilet = request.POST['stud_bilet'],
                                        stud_group = Group(pk=request.POST['stud_group'])
                )
            student_object.save()
            return redirect(u'/?status_message=Студент успішно відредагований!/')

    return render_to_response('edit_student.html', {
                                                    'table_student': table_student,
                                                    'table_group': Group.objects.all(),
                                                    'groups': groups},
                                                    context_instance=RequestContext(request)
    )

def edit_group(request, group_id):
    table_group = Group.objects.get(id=group_id)
    table_student = Student.objects.all()
    errors = {}
    error = {}
    if request.POST.get('name_group', '').strip() == '':
        errors['name_group'] = 'Введіть будь ласка назву групи'
        error['name_group'] = 'поле Назва групи обов’язкове'
    if request.POST.get('submit'):
        if errors:
            return render_to_response('edit_group.html', {
                                                          'errors': errors,
                                                          'error': error,
                                                          },
                                                          context_instance=RequestContext(request)
            )
        else:
            if request.POST.get('king_group', '').strip() == '':
                group_object = Group(id = group_id,
                                    name_group = request.POST['name_group'],
                                    king_group = None
                )
            else:
                group_object = Group(id = group_id,
                                    name_group = request.POST['name_group'],
                                    king_group = Student(pk=request.POST['king_group'])
                )
            group_object.save()
            return redirect('/groups/')
    return render_to_response('edit_group.html', {
                                                'table_student': table_student,
                                                'table_group': table_group},
                                                context_instance=RequestContext(request)
    )

def stud_delete(request, student_id):
    s = Student.objects.get(id=student_id)
    s.delete()
    return redirect(u'/?status_message=Студент успішно видалений!/')

def group_delete(request, group_id):
    g = Group.objects.get(id=group_id)
    g.delete()
    return redirect('/groups/')
