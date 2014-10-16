from django import forms
from django.forms import ModelForm
from models import Student, Group

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'middle_name', 'date', 'foto', 'stud_bilet', 'stud_group')

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ('name_group', 'king_group')