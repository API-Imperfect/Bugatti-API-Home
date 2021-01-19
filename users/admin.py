from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class UserAdmin(BaseUserAdmin):
    ordering=["id"]
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=CustomUser
    list_display=["email","name","is_staff","is_active"]
    list_filter=["email","name","is_staff","is_active"]
    fieldsets=(
        (_("Login Credentials"),{"fields":("email","password",)}),
        (_("Personal Information"),{"fields":("name",)}),
        (_("Permissions and Groups"),{"fields":("is_active","is_staff","is_superuser","groups", "user_permissions",)}),
        (_("Important dates"),{"fields":("last_login","date_joined",)}),
    )
    add_fieldsets=(
        (None,{"classes":("wide",),
        "fields":("email","name","password1","password2","is_staff","is_active")}),
    )
    search_fields=["email","name"]
    ordering=["email"]

admin.site.register(CustomUser,UserAdmin)    

