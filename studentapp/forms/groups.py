# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, ButtonHolder
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from studentapp.models.groups import Group

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
        FormActions(
                Submit('save', u'Зберегти'),
                Button('cancel', u'Назад'),
                css_class="buttons-form-submit"
            ),
    )