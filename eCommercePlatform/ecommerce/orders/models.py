from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from datetime import date


class Customer(models.Model):
    name = models.CharField(max_length=100, validators=[
        MinLengthValidator(3),
        RegexValidator(regex='^[a-zA-Z]+$', message='Name must contain alphabets only.')
    ])
    address = models.CharField(max_length=200, validators=[
        MinLengthValidator(10),
        RegexValidator(regex='^[a-zA-Z0-9 ]+$', message='Address must be alphanumeric.')
    ])

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.item_name} (x{self.quantity})"

