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
        r'^checkout/(?P<product_id>[\d]+)/$',
        order_views.CheckoutView.as_view(),
        name='checkout'
    ),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
