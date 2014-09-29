from django.shortcuts import render
from django.shortcuts import render_to_response
from studentapp.models import Student, TableGroup
from forms import StudentForm, TableGroupForm
from django.core.context_processors import csrf


# Create your views here.

def index(request):
    return render_to_response('index.html', {'table_student': Student.objects.all()})

def add_student(request):
    student_form = StudentForm
    args = {}
    args.update(csrf(request))
    args['form'] = student_form
    form.save()
    return render_to_response('add_student.html')

def add_group(request):
    return render_to_response('add_group.html')

