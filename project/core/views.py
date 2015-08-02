from django.shortcuts import render

def home(resquest):
    template_name = 'core/home.html'
    return render(resquest, template_name)