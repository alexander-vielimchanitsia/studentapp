# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth import get_user_model

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, ButtonHolder
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


User = get_user_model()

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

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user= User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError('Ви впевнені, що зареєстровані? Такого користувача не існує.')
        return username

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            user = None
        if user is not None and not user.check_password(password):
            raise forms.ValidationError('Невірний пароль')
        elif user is None:
            pass
        else:
            return password

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
                Submit('save', u'Увійти'),
                HTML(u'<a class="btn btn-default" href={% url "home" %}>Скасувати</a>'),
                css_class="buttons-form-submit",
                id="accounts-buttons",
            ),
        )

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']

    password1 = forms.CharField(
        widget=forms.PasswordInput(),
        label=u'Пароль',
        max_length=15
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label=u'Підтвердження пароля',
        max_length=15
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Паролі не співпадають')
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_count = User.objects.filter(email=email).count()
        if user_count > 0:
            raise forms.ValidationError('Ця почтова адреса вже зареєстрована іншим користувачем.')
        return email

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-registerForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-3'
        self.helper.layout = Layout(
            'username',
            'email',
            'password1',
            'password2',
            FormActions(
                Submit('save', u'Зареєструватись'),
                HTML(u'<a class="btn btn-default" href={% url "home" %}>Скасувати</a>'),
                css_class="buttons-form-submit",
                id="accounts-buttons",
            ),
        )

