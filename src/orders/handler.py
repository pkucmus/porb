import json


class CartPossition(object):

    def __init__(self, product_id, qty):
        self.product_id, self.qty = product_id, int(qty)

    def serialize(self):
        return {
            'id': self.product_id,
            'qty': self.qty
        }


class CartHandler(object):
    CART_KEY = 'cart'

    def __init__(self, request):
        self.request = request
        cart_data = json.loads(self.request.session.get(self.CART_KEY, '[]'))
        self.cart = [
            CartPossition(pos['id'], pos['qty']) for pos in cart_data
        ]

    def serialize(self):
        return [pos.serialize() for pos in self.cart]

    def commit(self):
        self.request.session[self.CART_KEY] = json.dumps(self.serialize())
        self.request.session.save()

    def get(self, product_id):
        result = filter(lambda pos: pos.product_id == product_id, self.cart)
        assert len(result) <= 1, 'Get returned more than one.'
        try:
            return result[0]
        except IndexError:
            return None

    def add(self, product_id, qty):
        position = self.get(product_id)
        if position:
            position.qty += int(qty)
        else:
            self.cart.append(CartPossition(product_id, qty))
        self.commit()
        return self.cart

    def remove(self, product_id, qty=0):
        position = self.get(product_id)
        if position:
            position.qty -= int(qty)
        if position.qty < 1 or qty == 0:
            self.cart.remove(position)
        self.commit()
        return self.cart
