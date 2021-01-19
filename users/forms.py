from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields=["email","name"]
        error_class="error"


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=["email","name"]
        error_class="error"        
