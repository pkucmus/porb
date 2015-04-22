# encoding: utf-8
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
    address = models.TextField()

    class Meta:
        verbose_name = 'zamówienie'
        verbose_name_plural = 'zamówienia'


class OrderPossitions(models.Model):
    order = models.ForeignKey(Order, related_name='order_possitions')
    product = models.ForeignKey(Product, related_name='order_possitions')
    qty = models.IntegerField()

    class Meta:
        verbose_name = 'pozycja'
        verbose_name_plural = 'pozycje'
