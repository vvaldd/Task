from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from core.managers import UserManager
from core.validators.custom_validator import validate


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
    password = models.CharField(max_length=20, validators=[validate])
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    user_type_choices = [
        ('admin', 'admin'),
        ('driver', 'driver')
    ]
    user_type = models.CharField(max_length=6, choices=user_type_choices, default=None)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    # objects connect with UserManager
    objects = UserManager()
