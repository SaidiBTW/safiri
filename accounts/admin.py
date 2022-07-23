from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
)
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email','username','phone_number','date_of_birth',]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('phone_number','date_of_birth',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields':('phone_number','date_of_birth',)}),
    )

admin.site.register(CustomUser,CustomUserAdmin)
