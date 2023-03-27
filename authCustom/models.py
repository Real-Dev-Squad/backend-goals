import binascii
import os
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .utils import env


class Token_Custom(models.Model):
    """
    The default authorization token model.
    """
    auth_token = models.CharField(_("Auth Token"), max_length=40)
    userId = models.CharField(primary_key=True, max_length=80)
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.auth_token:
            self.auth_token = self.generate_key()
        return super().save(*args, **kwargs)

    @classmethod
    def is_invalid(self, createdTime):
        curr_time = timezone.now().timestamp()
        auth_invalid_seconds = float(env('AUTH_TOKEN_INVALIDATION_TIME_IN_SECONDS'))
        exp_time = createdTime + auth_invalid_seconds
        if exp_time > curr_time:
            return False
        return True

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.auth_token
