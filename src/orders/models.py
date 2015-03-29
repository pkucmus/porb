from django.db import models

from customers.models import Customer
from products.models import Product


ORDER_STATUSES = (
    ('C', 'Cart'),
    ('O', 'Order'),
    ('P', 'Paid Order'),
    ('R', 'Realized'),
    ('X', 'Cancelled'),
)
UNIT_TYPES = (
    ('kg', 'kg'),
    ('pcs', 'pcs')
)


class Order(models.Model):
    status = models.CharField(choices=ORDER_STATUSES, max_length=1)
    # customer = models.ForeignKey(Customer, related_name='orders')

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    address_line = models.CharField(max_length=256)
    city = models.CharField(max_length=64)
    postal_code = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=20)

    email = models.EmailField()


class OrderPossition(models.Model):
    order = models.ForeignKey(Order, related_name='possitions')

    product = models.ForeignKey(Product, related_name='orders')
    qty = models.DecimalField(max_digits=13, decimal_places=2)
    unit_type = models.CharField(choices=UNIT_TYPES, max_length=3)
