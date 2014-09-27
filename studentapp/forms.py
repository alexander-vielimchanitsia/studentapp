from django import forms
from django.forms import ModelForm
from models import Student, TableGroup

class StudentForm(ModelForm):
    class Meta:
        model = Student

class TableGroupForm(ModelForm):
    class Meta:
        model = TableGroup