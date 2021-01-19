from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

"""A Manager is the interface through which database query operations are provided to Django models"""
class CustomUserAccountManager(BaseUserManager):
    # Custom user model manage with email as unique identifier
    def create_user(self,email,password,**extra_fields):
        # Create and save user with given email-password combination
        if not email:
            raise ValueError(_("The Email field is required"))
        email=self.normalize_email(email)
        user=self.model(email=email, **extra_fields)
        user.set_password(password)
        extra_fields.setdefault("is_staff",False)
        extra_fields.setdefault("is_superuser",False)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password,**extra_fields):
        # Create and save superuser with email-password combination
        extra_fields.setdefault("is_staff",True)    
        extra_fields.setdefault("is_superuser",True)    
        extra_fields.setdefault("is_active",True)  

        if extra_fields.get("is_staff") is not True:
            raise ValueError (_("SuperUsers must have is_staff=True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError (_("SuperUsers must have is_superuser=True"))  
        user=self.create_user(email,password,**extra_fields)
        user.save(using=self._db)
        return user

