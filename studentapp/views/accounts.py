from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate

from studentapp.forms.accounts import LoginForm


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

    context = {
        'form': form
    }
    return render(request, '../templates/accounts/login.html', context)