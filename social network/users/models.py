from django.contrib.auth.models import AbstractUser
from django.db import models


class AbstrapUser(AbstractUser):
    photo = models.ImageField(upload_to='profile_photos', null=True, blank=True)
