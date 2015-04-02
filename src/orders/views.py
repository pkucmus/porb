from django.views.generic import TemplateView
from django.shortcuts import render

from products.models import Product
from orders.models import Order
from orders.forms import CheckoutForm


class CheckoutView(TemplateView):
    template_name = 'checkout.html'

    def get_context_data(self, **kwargs):
        return {
            'product': Product.objects.get(pk=kwargs['product_id']),
            'form': CheckoutForm(initial={'product_id': kwargs['product_id']})
        }

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                status='O',
                product=Product.objects.get(pk=kwargs['product_id']),
                address=form.data['address']
                )
            return render(request, 'checkout_done.html', {'order': order})
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)
