from django import forms
from django.forms import ModelForm
from models import Student, TableGroup

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class TableGroupForm(ModelForm):
    class Meta:
        model = TableGroup
        fields = ['name_group', 'king_group', 'student']