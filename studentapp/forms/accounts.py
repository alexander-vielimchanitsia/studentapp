# -*- coding: utf-8 -*-

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label=u'Ім’я користувача',
        max_length=15)
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label=u'Пароль',
        max_length=15)