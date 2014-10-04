from django import forms
from django.forms import ModelForm
from models import Student, Group

class StudentForm(ModelForm):
    class Meta:
        model = Student
    

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name_group', 'king_group']