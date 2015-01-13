# -*- coding: utf-8 -*-

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, ButtonHolder
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class LoginForm(forms.Form):
    username = forms.CharField(
        label=u'Ім’я користувача',
        max_length=15
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label=u'Пароль',
        max_length=15
    )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-loginForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-3'
        self.helper.layout = Layout(
            'username',
            'password',
            FormActions(
                Submit('save', u'Зберегти'),
                HTML(u'<a class="btn btn-default" href={% url "home" %}>Скасувати</a>'),
                css_class="buttons-form-submit",
                id="accounts-buttons",
            ),
        )