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
    list_display = ('pk', 'address', 'status', )
    list_filter = ('status', )
    search_fields = ('address', )

admin.site.register(Order, OrderAdmin)
