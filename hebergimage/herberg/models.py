from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    user = models.ForeignKey(User, related_name="images")
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()

    def __str__(self):
        return self.image.name
