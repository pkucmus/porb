from django.db import models
from django.conf import settings

# class Category(models.Model):
#     parent = models.ForeignKey('self', related_name='sub_categories')
#     name = models.CharField(max_length=128)

#     @property
#     def products(self):
#         return self.products.all()


class AttributeType(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Attribute(models.Model):
    attribute_type = models.ForeignKey(AttributeType)
    value = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return u'{} - {}'.format(self.attribute_type.name, self.value)


class Product(models.Model):
    name = models.CharField(max_length=128)
    # category = models.ForeignKey(Category, related_name='products')
    description = models.TextField(null=True, blank=True)
    attribute = models.ManyToManyField(Attribute, related_name=u'attributes')
    price_gross = models.DecimalField(max_digits=13, decimal_places=4)

    # tax_percentage = models.IntegerField()

    # @property
    # def price_gross(self):
    #     return self.price_net + (self.price_net * self.tax_percentage / 100)

    def __unicode__(self):
        return u'{}'.format(self.name)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images')
    image = models.ImageField(
        upload_to='products/',
        verbose_name='photo'
    )
