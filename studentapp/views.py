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
    form = student_form
    return render_to_response('add_student.html', {'form': form}, context_instance=RequestContext(request))

def add_group(request):
    return render_to_response('add_group.html')

def addstudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            student.save()
    return redirect('/')
