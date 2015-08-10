from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import authenticate, login, get_user_model

from .forms import RegisterForm, PasswordResetForm
from .models import PasswordReset 

def timer(resquest):
    template_name = 'timer.html'
    return render(resquest, template_name)

def register(resquest):
    template_name = 'register.html'
    if resquest.method == 'POST':
        form = RegisterForm(resquest.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                email=user.email, password= form.cleaned_data['password1']
            )
            login(resquest, user)
            return redirect('core:timer')
    else:
        form = RegisterForm()
    context = {
        'form' : form
    }
    return render(resquest, template_name, context)

def password_reset(resquest):
    template_name = 'password_reset.html'
    context = {}
    form = PasswordResetForm(resquest.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(resquest, template_name, context)

def password_reset_confirm(resquest, key):
    template_name = 'password_reset_confirm.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=resquest.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(resquest, template_name, context) 