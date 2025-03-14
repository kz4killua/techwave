from django.db import models
from django.core.validators import MinValueValidator


class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])


    def __str__(self):
        return self.name
