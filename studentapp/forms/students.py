# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django import forms
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, ButtonHolder
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from studentapp.models import Student

class StudentFormAdd(ModelForm):
    class Meta:
        model = Student
        exclude = []

    def __init__(self, *args, **kwargs):
        super(StudentFormAdd, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-student-form'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('add_student')
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-2 field_retreat'
        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'middle_name',
            Field('date', data_date_format="yyyy-mm-dd", placeholder='рррр-мм-дд'),
            'foto',
            'stud_bilet',
            'stud_group',
            FormActions(
                Submit('save_button_add', u'Зберегти', css_class="btn btn-primary"),
                Submit('cancel_button_add', u'Скасувати', css_class="btn btn-link"),
                css_class="buttons-form-submit"
            ),
        )

class StudentFormEdit(ModelForm):
    class Meta:
        model = Student
        exclude = []

    def __init__(self, *args, **kwargs):
        super(StudentFormEdit, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-student-form'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('edit_student',
            kwargs={'pk': kwargs['instance'].id})
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-2 field_retreat'
        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'middle_name',
            Field('date', data_date_format="yyyy-mm-dd", placeholder='рррр-мм-дд'),
            'foto',
            'stud_bilet',
            'stud_group',
            FormActions(
                Submit('save_button_edit', u'Зберегти', css_class="btn btn-primary"),
                Submit('cancel_button_edit', u'Скасувати', css_class="btn btn-link"),
                css_class="buttons-form-submit"
            ),
        )