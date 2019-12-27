from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import PBKDF2PasswordHasher


class CustomUser(AbstractUser):

    def save(self, *args, **kwargs):
        hasher = PBKDF2PasswordHasher()
        pwd_hash = hasher.encode(self.password, hasher.salt(), 150000)
        self.password = pwd_hash
        super(AbstractUser, self).save(*args, **kwargs)
