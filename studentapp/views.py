from django.shortcuts import render
from django.shortcuts import render_to_response
from studentapp.models import Student, TableGroup
from forms import StudentForm, TableGroupForm


# Create your views here.

def index(request):
    student_form = StudentForm
    args = {}
    args['studentapp_student'] = Student.objects.all()
    args['form'] = student_form
    return render_to_response('index.html')

def add_student(request):
    return render_to_response('add_student.html')

def add_group(request):
    return render_to_response('add_group.html')

