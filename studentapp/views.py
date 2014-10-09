# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from studentapp.models import Student, Group
from forms import StudentForm, GroupForm
from django.core.context_processors import csrf
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
    if request.POST:
        first_name = request.POST.get('name_group', '')
        last_name = request.POST.get('last_name', '')
        middle_name = request.POST.get('middle_name', '')
        date = request.POST.get('date', '')
        foto = request.POST.get('foto', '')
        stud_bilet = request.POST.get('stud_bilet', '')
        stud_group = request.POST.get('stud_group', '')
        if student_form.is_valid():
            student_form.save()
            return redirect('/')
        else:
            studet_form = StudentForm()
        return render(request, 'add_student.html', { 'student_form': student_form })

def addgroup(request):
    group_form = GroupForm(request.POST)
    if group_form.is_valid():
        group_form.save()
        return redirect('/')
    else:
        group_form = GroupForm()
    return render(request, 'add_group.html', { 'group_form': group_form })
        
    
