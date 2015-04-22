from django.contrib import admin

from products.models import (
    Product,
    Attribute,
    AttributeType,
    ProductImage,
    Category,
)


class ProductImageInline(admin.StackedInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]
    list_display = ('name', 'category', 'price_gross', )
    list_filter = ('attribute', 'category', )
    search_fields = ('name', 'description', )

admin.site.register(AttributeType)
admin.site.register(Attribute)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
