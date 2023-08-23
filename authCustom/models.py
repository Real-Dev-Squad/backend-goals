import binascii
import os
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from base.utils import env
from base.models import BaseModel

class Token_Custom(BaseModel):
    """
    The default authorization token model.
    """
    auth_token = models.CharField(_("Auth Token"), max_length=40)
    user_id = models.CharField(max_length=80)
    token_created = models.DateTimeField(_("Token Created"), auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.auth_token:
            self.auth_token = self.generate_key()
        return super().save(*args, **kwargs)

    def is_invalid(self):
        curr_time = timezone.now().timestamp()
        auth_invalid_seconds = float(env('AUTH_TOKEN_INVALIDATION_TIME_IN_SECONDS'))
        exp_time = self.token_created.timestamp() + auth_invalid_seconds
        if exp_time > curr_time:
            return False
        return True
    
    def update_token(self):
        self.auth_token = self.generate_key()
        self.token_created=timezone.now()
        return self.save()

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.auth_token
