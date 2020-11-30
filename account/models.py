from django.db import models
from django.contrib.auth.models import BaseUserManager ,AbstractBaseUser,PermissionsMixin
from django.db.models.fields import BooleanField
from django.utils.translation import gettext as _

# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations=True

    def create_user(self,email,name,password=None):
        user =self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.is_active=True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self,email,name,password):
        user =self.create_user(
            email,
            password=password,
            name=name,
        )

        user.is_active=True
        user.is_staff=True
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,name,password):
        user=self.create_user(
            email,
            name=name,
            password=password,
        )
        user.is_active=True
        user.is_superuser=True
        user.is_staff=True
        user.admin=True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser,PermissionsMixin):
    username=None
    email=models.EmailField(_('email address'),unique=True)
    name=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS=['name']
    objects=UserManager()

    def __str__(self):
        return self.email