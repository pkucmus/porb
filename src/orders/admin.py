from django.contrib import admin

from orders.models import (
    Order,
    OrderPossitions,
)


class OrderPossitionsInline(admin.StackedInline):
    model = OrderPossitions


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderPossitionsInline,
    ]
    list_display = (
        'pk', 'name', 'address_line_1', 'city', 'post_code', 'email', 'status',
    )
    list_filter = ('status', )
    search_fields = ('name', 'address_line_1', 'city', 'post_code', 'email', )

admin.site.register(Order, OrderAdmin)
