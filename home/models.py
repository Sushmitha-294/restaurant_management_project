from django.db import models

class MenuCategory(models.Model):
    name = models.CharField(max_length = 100 , unique =True)
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length =100)
    price = models.DecimalField(max_digits=8,decimal_places)
    description = models.TextField()
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)

    has_delivery = models.BooleanField(default=False)

    def __str__(self):
        return self.name