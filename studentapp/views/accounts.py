# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponseRedirect, render_to_response, redirect
from django.contrib.auth import logout, login, authenticate
from django.core.urlresolvers import reverse

from studentapp.forms.accounts import RegistrationForm


def logout_view(request):
    logout(request)

    return HttpResponseRedirect(reverse('home'))

def registration_view(request):
    form = RegistrationForm(request.POST or None)

    if form.is_valid():
        form.save()

        return redirect(u'%s?status_message=Користувач успішно зареєстрований!' %
                        reverse('home'))

    context = {
        'form': form
    }

    return render(request, 'accounts/register.html', context)