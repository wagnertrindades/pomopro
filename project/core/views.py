from django.shortcuts import render

def timer(resquest):
    template_name = 'timer.html'
    return render(resquest, template_name)

