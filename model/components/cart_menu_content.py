from selene.elements import SeleneElement

from model.components.cart_menu_item import CartMenuItem


class CartMenuContent:
    def __init__(self, element: SeleneElement):
        self.element = element

    @property
    def items(self):
        return self.element.find_all(".products dt")

    def item(self, index: int) -> CartMenuItem:
        return CartMenuItem(self.items[index-1])

    @property
    def total_price(self):
        return self.element.find(".ajax_block_cart_total")

    def check_out(self):
        self.element.find("#button_order_cart").click()
