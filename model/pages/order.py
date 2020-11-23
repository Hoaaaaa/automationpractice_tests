from selene.support.conditions import be

from model.components.cart import Cart


class Order:
    cart: Cart = Cart()

    def should_not_have_cart(self):
        self.cart.element.should_not(be.in_dom)
