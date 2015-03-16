# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth import get_user_model

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML
from crispy_forms.bootstrap import FormActions


User = get_user_model()

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
            raise forms.ValidationError(
                'Ця почтова адреса вже зареєстрована іншим користувачем.')

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
                HTML(u'<a class="btn btn-default" href={% url "home" %}> \
                    Скасувати</a>'),
                css_class="buttons-form-submit",
                id="accounts-buttons",
            ),
        )

