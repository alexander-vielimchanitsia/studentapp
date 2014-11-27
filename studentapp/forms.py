from django import forms
from django.forms import ModelForm
from models import Student, Group
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class StudentForm(ModelForm):
    class Meta:
        model = Student
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-student-form'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = '/addstudent/'
        self.helper.add_input(Submit('submit', 'Submit', css_class="buttons-form"))
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-2'
        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'middle_name',
            'date',
            'foto',
            'stud_bilet',
            'stud_group',
        )

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