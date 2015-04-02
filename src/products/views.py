from django.views.generic import TemplateView

from products.models import Product


class HomepageView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        return {
            'products': Product.objects.all()
        }


class ProductView(TemplateView):
    template_name = 'product_details.html'

    def get_context_data(self, **kwargs):
        return {
            'product': Product.objects.get(pk=kwargs['product_id'])
        }
