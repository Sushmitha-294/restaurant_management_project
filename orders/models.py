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

    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='orders'
    )

    created_at =models.DateTimeField(auto_now_add =True)
    total_price = models.DecimalField(max_digits =10,decimal_places=2)
    def __str__(self):
        return self.code