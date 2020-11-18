from selene.support.conditions import be

from model.components.cart import Cart


class OrderPage:
    Cart = Cart()

    def should_not_have_cart(self):
        self.Cart.element.should_not(be.in_dom)
