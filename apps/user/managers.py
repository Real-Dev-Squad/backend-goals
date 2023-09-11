from django.contrib.auth.models import BaseUserManager
import string
from django.utils.crypto import get_random_string


class UserManager(BaseUserManager):
    def create_user(self, rds_id, password=None, **extra_fields):
        if not rds_id:
            raise ValueError('The rds_id field must be set')
        user = self.model(rds_id=rds_id, **extra_fields)
        if password is None:
            password = self._generate_random_password()
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, rds_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(rds_id, password, **extra_fields)
    
    @staticmethod
    def _generate_random_password():
        length = 50  # You can adjust the password length as needed
        chars = string.ascii_letters + string.digits + string.punctuation
        return get_random_string(length, chars)
