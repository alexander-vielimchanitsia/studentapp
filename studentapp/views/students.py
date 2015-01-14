# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from studentapp.models.groups import Group
from studentapp.models.students import Student
from studentapp.forms import StudentFormAdd, StudentFormEdit


def students_list(request, page_number=1):
    table_student = Student.objects.all()

    # try ro order students list
    order_by = request.GET.get('order_by', 'last_name')
    if order_by in ('id', 'last_name', 'first_name'):
        table_student = table_student.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            table_student = table_student.reverse()

    paginator = Paginator(table_student, 3)
    page = request.GET.get('page')
    try:
        table_student = paginator.page(page)
    except PageNotAnInteger:
        table_student = paginator.page(1)
    except EmptyPage:
        table_student = paginator.page(paginator.num_pages)
    return render_to_response('students/students_list.html',
        {'table_student': table_student},
        context_instance=RequestContext(request))

def add_student(request):
    if request.POST:
        form = StudentFormAdd(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(u'%s?status_message=Студент успішно доданий!' %
                            reverse('home'))

        # activity if click on save button
        if request.POST.get('cancel_button_add') is not None:
            # redirect to home page on cancel button
            return HttpResponseRedirect(
                u'%s?status_message=Додавання студента скасовано!' %
                reverse('home'))
    else:
        form = StudentFormAdd()
    return render(request, 'students/add_student.html',
        {'form': form})

def edit_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        # activity if click on save button
        if request.POST.get('save_button_edit') is not None:
            form = StudentFormEdit(request.POST, request.FILES, instance=student)
            if form.is_valid():
                student = form.save()
                return redirect(u'%s?status_message=Студент успішно відредагований!' %
                                reverse('home'))

        elif request.POST.get('cancel_button_edit') is not None:
            # redirect to home page on cancel button
            return HttpResponseRedirect(
                u'%s?status_message=Редагування студента скасовано!' %
                reverse('home'))
    else:
        form = StudentFormEdit(instance=student)
    return render_to_response('students/edit_student.html',
        {'form': form,
        'student': student},
        context_instance=RequestContext(request))

def stud_delete(request, student_id):
    s = Student.objects.get(id=student_id)

    s.delete()

    return redirect(u'%s?status_message=Студент успішно видалений!' %
                    reverse('home'))