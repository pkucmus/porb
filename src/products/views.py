from django.views.generic import TemplateView

from products.models import Product
from products.forms import SearchForm


class HomepageView(TemplateView):
    template_name = 'homepage.html'

    def get_queryset(self):
        query_params = self.request.GET

        filter_kwargs = {}
        if query_params.get('name'):
            filter_kwargs['name__icontains'] = query_params['name']
        if query_params.get('categories'):
            filter_kwargs['category__pk'] = query_params['categories']
        if query_params.get('price_from'):
            filter_kwargs['price_gross__gte'] = query_params['price_from']
        if query_params.get('price_to'):
            filter_kwargs['price_gross__lte'] = query_params['price_to']

        return Product.objects.filter(**filter_kwargs)

    def get_context_data(self, **kwargs):
        return {
            'search_form': SearchForm(self.request.GET),
            'products': self.get_queryset(),
        }


class ProductView(TemplateView):
    template_name = 'product_details.html'

    def get_context_data(self, **kwargs):
        return {
            'product': Product.objects.get(pk=kwargs['product_id']),
        }
