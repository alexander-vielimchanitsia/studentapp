# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django import forms
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, ButtonHolder
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from studentapp.models import Student, Group

class GroupFormAdd(ModelForm):
    class Meta:
        model = Group
        exclude = []

    def __init__(self, *args, **kwargs):
        super(GroupFormAdd, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-group-form'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('add_group')
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-2 field_retreat'
        self.helper.layout = Layout(
            Field('name_group'),
            FormActions(
                Submit('save', u'Зберегти'),
                HTML(u'<a class="btn btn-default" href={% url "group_list" %}>Скасувати</a>'),
                css_class="buttons-form-submit"
            ))

class GroupFormEdit(ModelForm):
    class Meta:
        model = Group
        exclude = []

    def clean_king_group(self):
        #Check if student in the group.
        students = Student.objects.filter(stud_group=self.instance)
        if len(students) > 0 and \
            not self.cleaned_data['king_group'] == None and \
            self.cleaned_data['king_group'] != students[0]:
            raise forms.ValidationError(u'Студент не є учасником цієї групи.',
                code='invalid')

        return self.cleaned_data['king_group']

    def __init__(self, *args, **kwargs):
        super(GroupFormEdit, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-group-form'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('edit_group',
            kwargs={'pk': kwargs['instance'].id})
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-2 field_retreat'
        self.helper.layout = Layout(
            Field('name_group'),
            'king_group',
            FormActions(
                Submit('save', u'Зберегти'),
                HTML(u'<a class="btn btn-default" href={% url "group_list" %}>Скасувати</a>'),
                css_class="buttons-form-submit"
            ))