from django import forms
from django.forms import ModelForm
from models import Student, Group
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class StudentForm(ModelForm):
    class Meta:
        model = Student
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-2'
    helper.button_class = 'col-lg-1'
    helper.layout = Layout(
        'first_name',
        'last_name',
        'middle_name',
        'date',
        'foto',
        'stud_bilet',
        'stud_group',
    )
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = '/index/addstudent/'
        self.helper.add_input(Submit('submit', 'Submit'))

class GroupForm(ModelForm):
    class Meta:
        model = Group
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-2'
    helper.layout = Layout(
        'name_group',
        'king_group',
    )