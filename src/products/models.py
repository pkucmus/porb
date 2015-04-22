# encoding: utf-8
from django.db import models

from sorl.thumbnail import ImageField


class Category(models.Model):
    parent = models.ForeignKey(
        'self',
        related_name='sub_categories', null=True, blank=True
    )
    name = models.CharField(max_length=128)

    @property
    def products(self):
        return self.products.all()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'kategoria'
        verbose_name_plural = 'kategorie'


class AttributeType(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'typ atrybutu'
        verbose_name_plural = 'typy atrybutów'


class Attribute(models.Model):
    attribute_type = models.ForeignKey(AttributeType)
    value = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return u'{} - {}'.format(self.attribute_type.name, self.value)

    class Meta:
        verbose_name = 'atrybut'
        verbose_name_plural = 'atrybuty'


class Product(models.Model):
    name = models.CharField(max_length=128)
    category = models.ForeignKey(Category, related_name='products')
    description = models.TextField(null=True, blank=True)
    attribute = models.ManyToManyField(Attribute, related_name=u'attributes')
    price_gross = models.DecimalField(max_digits=13, decimal_places=4)

    class Meta:
        verbose_name = 'produkt'
        verbose_name_plural = 'produkty'

    def __unicode__(self):
        return u'{}'.format(self.name)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images')
    image = ImageField(
        upload_to='products/',
        verbose_name='photo'
    )

    class Meta:
        verbose_name = 'zdjęcie'
        verbose_name_plural = 'zdjęcia'
