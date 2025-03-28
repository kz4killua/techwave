from django.db import models  # Import Django's model framework
from django.core.validators import MinValueValidator  # Import validator to enforce minimum values


# Define the Item model to represent inventory items
class Item(models.Model):
    name = models.CharField(
        max_length=100,  # Maximum length of 100 characters
        unique=True  # Ensures that each item name is unique
    )
    stock = models.PositiveIntegerField()  # Ensures only non-negative whole numbers for stock quantity
    price = models.DecimalField(
        max_digits=10,  # Allows up to 10 digits in total
        decimal_places=2,  # Ensures two decimal places for currency representation
        validators=[MinValueValidator(0.01)]  # Enforces a minimum price of 0.01 (no free items)
    )
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)

    def __str__(self):
        return self.name  # Returns the item name when the object is printed or displayed
