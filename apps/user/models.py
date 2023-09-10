from django.db import models
# from django.contrib.postgres.fields import JSONField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from apps.base.models import BaseModel
from apps.user.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    rds_id = models.CharField(max_length=80, unique=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'rds_id'

    def __str__(self):
        return self.rds_id
