from django.db import models
from django.contrib.auth.models import AbstractUser


def path_to_avatar(instance, filename):
    return f'avatars/{instance.id}/{filename}'
class CustomUser(AbstractUser):
    email = models.EmailField(
    max_length=150, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    avatar = models.ImageField(
        upload_to=path_to_avatar, null=True, blank=True)
