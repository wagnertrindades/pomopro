from django.shortcuts import render

def home(resquest):
    template_name = 'accounts/home.html'
    return render(resquest, template_name)