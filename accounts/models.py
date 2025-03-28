from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)  # Field for the image

    def __str__(self):
        return self.name