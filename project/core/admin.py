from django.contrib import admin

from .models import Timer

class TimerAdmin(admin.ModelAdmin):

	list_display = ['status', 'user', 'created_at']

admin.site.register(Timer, TimerAdmin)