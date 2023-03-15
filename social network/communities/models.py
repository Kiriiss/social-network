from django.db import models
from users.models import AbstrapUser

class Community(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='community_photos/')
    creator = models.ForeignKey(AbstrapUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name