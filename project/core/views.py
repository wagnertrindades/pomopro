from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Timer

@login_required
def timer(resquest):
    template_name = 'timer.html'
    return render(resquest, template_name)

@login_required
def add_timer(resquest, status):
	Timer(status=status, user=resquest.user).save()
	return redirect('core:timer')