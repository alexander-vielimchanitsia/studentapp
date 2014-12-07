# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, ButtonHolder
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from studentapp.models import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-student-form'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = '/students/add/'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-2'
        self.helper.form_tag = 'data-toggle="validator"'
        self.helper.layout = Layout(
            Field('first_name', pattern="^([_A-z0-9]){3,}$"),
            'last_name',
            'middle_name',
            'date',
            'foto',
            'stud_bilet',
            'stud_group',
            FormActions(
                Submit('save', u'Зберегти'),
                Button('cancel', u'Назад'),
                css_class="buttons-form-submit"
            ),
        )