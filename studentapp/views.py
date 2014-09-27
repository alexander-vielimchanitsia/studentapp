from django.shortcuts import render
from django.shortcuts import render_to_response
from studentapp.models import Student, TableGroup
# Create your views here.
def index(request):
    return render_to_response('index.html', {'studentapp_student': Student.objects.all()})

def add_student(request):
    return render_to_response('add_student.html')

def add_group(request):
    return render_to_response('add_group.html')