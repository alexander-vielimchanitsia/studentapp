from django.shortcuts import render
from django.shortcuts import render_to_response
from studentapp.models import Student, Group
from forms import StudentForm, GroupForm
from django.core.context_processors import csrf
from django.views.generic.edit import CreateView, UpdateView


# Create your views here.


def index(request):
    return render_to_response('index.html', {'table_student': Student.objects.all(), 'table_group': Group.objects.all()})

def add_student(request):
    student_form = StudentForm
    args = {}
    args.update(csrf(request))
    args['form'] = student_form
    return render_to_response('add_student.html')

def add_group(request):
    return render_to_response('add_group.html')

def addstudent(request):
    if request.POST:
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            form.save()
    return redirect('/index/')

class StudentCreate(CreateView):
    model = Student
    fields = ['first_name', 'last_name', 'middle_name', 'date', 'foto', 'stud_bilet', 'stud_group']

class StudentUpdate(UpdateView):
    model = Student
    fields = ['first_name', 'last_name', 'middle_name', 'date', 'foto', 'stud_bilet', 'stud_group']
