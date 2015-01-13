# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponseRedirect, render_to_response, redirect
from django.contrib.auth import logout, login, authenticate

from studentapp.forms.accounts import LoginForm, RegistrationForm


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect(u'/?status_message=Авторизація пройшла успішно!')

    context = {
        'form': form
    }
    return render(request, '../templates/accounts/login.html', context)

def registration_view(request):
    form = RegistrationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(u'/?status_message=Користувач успішно зареєстрований!')

    context = {
        'form': form
    }
    return render(request, '../templates/accounts/register.html', context)