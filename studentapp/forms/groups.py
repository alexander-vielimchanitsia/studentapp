# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, ButtonHolder
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from studentapp.models import Group

class GroupForm(ModelForm):
    class Meta:
        model = Group
    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-group-form'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = '/groups/add/'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-2 field_retreat'
        self.helper.layout = Layout(
            Field('name_group', required=''),
            'king_group',
            FormActions(
                Submit('save', u'Зберегти'),
                HTML(u'<a class="btn" href={% url "group_list" %}>Скасувати</a>'),
                css_class="buttons-form-submit"
            ))