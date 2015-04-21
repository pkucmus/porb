from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from products import views as product_views
from orders import views as order_views

urlpatterns = patterns(
    '',
    url(r'^$', product_views.HomepageView.as_view(), name='home'),
    url(
        r'^product/(?P<product_id>[\d]+)/$',
        product_views.ProductView.as_view(),
        name='product_details'
    ),
    url(
        r'^cart/(?P<product_id>[\d]+)/$',
        order_views.CartView.as_view(),
        name='cart'
    ),
    url(
        r'^cart/(?P<product_id>[\d]+)/delete/$',
        order_views.DeleteCartView.as_view(),
        name='cart_delete'
    ),
    url(
        r'^checkout/$',
        order_views.CheckoutView.as_view(),
        name='checkout'
    ),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
