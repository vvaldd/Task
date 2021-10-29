from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from core.managers import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin):
    # create UserModel
    class Meta:
        db_table = 'auth_user'
        app_label = 'core'
    # describe needed fields
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=20)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    # objects connect with UserManager
    objects = UserManager()
