from django.db import models


# class Category(models.Model):
#     parent = models.ForeignKey('self', related_name='sub_categories')
#     name = models.CharField(max_length=128)

#     @property
#     def products(self):
#         return self.products.all()


class Product(models.Model):
    name = models.CharField(max_length=128)
    # category = models.ForeignKey(Category, related_name='products')

    price_gross = models.DecimalField(max_digits=13, decimal_places=4)
    # tax_percentage = models.IntegerField()

    # @property
    # def price_gross(self):
    #     return self.price_net + (self.price_net * self.tax_percentage / 100)
