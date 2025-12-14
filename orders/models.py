from django.db import models

# Create your models here.
class OrderSatus(models.Model):
    name = models.CharField(max_length =50, unique=True)
    def __str__(self):
        return self.code
class Order(models.Model):
    status = models.ForeignKey(
        OrderStatus,
        on_delete = models.SET_NULL,
        null =True,
        blank =True
    )
    def __str__(self):
        return self.code