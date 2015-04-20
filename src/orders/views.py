from django.views.generic import View, TemplateView
from django.shortcuts import render, redirect

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


class CartView(View):

    def post(self, request, *args, **kwargs):
        is_in_cart = False
        if 'cart' not in request.session:
            request.session['cart'] = []
        for position in request.session['cart']:
            if position['id'] == kwargs['product_id']:
                position['quantity'] += 1
                is_in_cart = True
        if not is_in_cart:
            request.session['cart'].append(
                {
                    'id': kwargs['product_id'],
                    'qty': 1
                }
            )
        return redirect('checkout')
