from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model

from .forms import RegisterForm 

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

