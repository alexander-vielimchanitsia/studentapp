from django.shortcuts import render
from django.shortcuts import render_to_response
from studentapp.models import Student, Group
from forms import StudentForm, GroupForm
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import redirect


# Create your views here.


def index(request):
    table_student = Student.objects.all()
    table_group = Group.objects.all()
    return render_to_response('index.html', {'table_student': table_student, 'table_group': table_group})

def add_student(request):
    student_form = StudentForm()
    return render_to_response('add_student.html', {'student_form': student_form}, context_instance=RequestContext(request))

def add_group(request):
    group_form = GroupForm()
    return render_to_response('add_group.html', {'group_form': group_form}, context_instance=RequestContext(request))

def addstudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('/')

def addgroup(request):
    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('/')
