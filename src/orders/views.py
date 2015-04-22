from django.views.generic import View, TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from products.models import Product
from products.forms import SearchForm

from orders.models import (
    Order,
    OrderPossitions,
)
from orders.forms import CheckoutForm
from orders.handler import CartHandler


class CheckoutView(TemplateView):
    template_name = 'checkout.html'

    def get_context_data(self):
        positions = []
        cart_sum = 0

        cart_handler = CartHandler(self.request)
        for position in cart_handler.cart:
            product = Product.objects.get(pk=position.product_id)
            position_sum = product.price_gross * position.qty
            cart_sum += position_sum
            positions.append(
                {
                    'product': product,
                    'quantity': position.qty,
                    'sum': position_sum,
                }
            )

        return {
            'positions': positions,
            'form': CheckoutForm(),
            'search_form': SearchForm(self.request.GET),
            'cart_sum': cart_sum,
        }

    def post(self, request, *args, **kwargs):
        cart_handler = CartHandler(self.request)
        form = CheckoutForm(request.POST)
        if form.is_valid() and cart_handler.cart:
            order = Order.objects.create(
                status='O',
                name=form.data['name'],
                address_line_1=form.data['address_line_1'],
                city=form.data['city'],
                post_code=form.data['post_code'],
                email=form.data['email'],
            )
            for position in cart_handler.cart:
                product = Product.objects.get(pk=position.product_id)
                order_position = OrderPossitions(
                    product=product,
                    qty=position.qty
                )
                order.order_possitions.add(order_position)
                cart_handler.purge()
            return render(
                request, 'checkout_done.html', {
                    'order': order,
                    'search_form': SearchForm(),
                })
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)


class CartView(View):
    def get(self, request, *args, **kwargs):
        cart_handler = CartHandler(request)
        cart_handler.add(request.GET['product_id'], request.GET.get('qty', 1))
        return HttpResponseRedirect(reverse('checkout'))


class DeleteCartView(View):
    def get(self, request, *args, **kwargs):
        cart_handler = CartHandler(request)
        cart_handler.remove(
            request.GET['product_id'], request.GET.get('qty', 0)
        )
        return HttpResponseRedirect(reverse('checkout'))
