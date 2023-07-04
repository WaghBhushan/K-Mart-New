from django.contrib import admin
from .models import UserProfile
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','mobile']
    search_fields = ['user__first_name','user__last_name']


admin.site.register(UserProfile,UserProfileAdmin)