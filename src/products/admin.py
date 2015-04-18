from django.contrib import admin

from products.models import Product, Attribute, AttributeType, ProductImage


class ProductImageInline(admin.StackedInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]

admin.site.register(ProductImage)
admin.site.register(AttributeType)
admin.site.register(Attribute)
admin.site.register(Product, ProductAdmin)
