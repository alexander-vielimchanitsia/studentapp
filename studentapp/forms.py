from django import forms
from django.forms import ModelForm
from models import Student, Group
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'middle_name', 'date', 'foto', 'stud_bilet', 'stud_group')
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-8'
    helper.layout = Layout(
        'first_name',
        'last_name',
        'middle_name',
        'date',
        'foto',
        'stud_bilet',
        'stud_group'
    )

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ('name_group', 'king_group')