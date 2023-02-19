from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(Uslugi)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Персональная информация', {
            'fields': ('first_name', 'last_name', 'patronomyc', 'avatar')}
        ),
        ('Остальная информация',
            {
                'classes': ('wide',),
                'fields': ('email', 'username', 'password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined'), }
        ),
    )
admin.site.register(Status)
admin.site.register(Order)
# Register your models here.
