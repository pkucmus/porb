from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    address_line = models.CharField(max_length=256)
    city = models.CharField(max_length=64)
    postal_code = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=20)

    email = models.EmailField()

    allows_newsletter = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
