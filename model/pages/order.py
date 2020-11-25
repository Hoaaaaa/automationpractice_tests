from selene.support.conditions import be

from model.components.cart import Cart
from model.components.cart_menu import CartMenu


class Order:
    cart: Cart = Cart()
    cart_menu: CartMenu = CartMenu()

    def should_not_have_cart(self):
        self.cart.element.should_not(be.in_dom)


order: Order = Order()
