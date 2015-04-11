from django.contrib import admin

from products.models import Product, Attribute, AttributeType, ProductImage


admin.site.register(ProductImage)
admin.site.register(AttributeType)
admin.site.register(Attribute)
admin.site.register(Product)
