from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model

def timer(resquest):
    template_name = 'timer.html'
    return render(resquest, template_name)

def register(resquest):
    template_name = 'home.html'
    if resquest.method == 'POST':
        if "register" in resquest.POST:
            form_register = RegisterForm(resquest.POST, prefix='register')
            if form_register.is_valid():
                user = form_register.save()
                user = authenticate(
                    email=user.email, password= form_register.cleaned_data['password1']
                )
                login(resquest, user)
                return redirect('core:timer')
    else:
        form_register = RegisterForm(prefix='register')
    context = {
        'form_register' : form_register
    }
    return render(resquest, template_name, context)