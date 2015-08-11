from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def timer(resquest):
    template_name = 'timer.html'
    return render(resquest, template_name)

