from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model

def timer(resquest):
    template_name = 'timer.html'
    return render(resquest, template_name)