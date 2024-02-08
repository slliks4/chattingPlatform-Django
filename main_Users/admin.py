from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile

class Profile_inline(admin.StackedInline):
    model = Profile

class User_model(admin.ModelAdmin):
    model = User
    list_display = ('email','username','date_joined','is_superuser')
    search_fields = ('email','username','first_name')
    fieldsets = (
        ('User settings', {'fields': ('email', 'username')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Groups', {'fields': ('groups',)}),
    ) 
    inlines = [Profile_inline]

admin.site.unregister(User)
admin.site.register(User,User_model)
