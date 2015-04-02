from django.db import models

from products.models import Product


ORDER_STATUSES = (
    ('C', 'Cart'),
    ('O', 'Order'),
    ('P', 'Paid Order'),
    ('R', 'Realized'),
    ('X', 'Cancelled'),
)


class Order(models.Model):
    status = models.CharField(choices=ORDER_STATUSES, max_length=1)
    product = models.ForeignKey(Product, related_name='orders')

    address = models.TextField()
