from django.contrib import admin

from .models import User 

class UserAdmin(admin.ModelAdmin):

    list_display = ['name', 'email', 'date_birth', 'created_at', 'updated_at', 'is_staff']
    search_fields = ['name', 'email']

admin.site.register(User, UserAdmin)