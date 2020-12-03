from selene.elements import SeleneElement
from selene.support.conditions import have

from model.components.cart_menu_item import CartMenuItem
from model.components.product import Product


class CartMenuContent:
    def __init__(self, element: SeleneElement):
        self.element = element

    @property
    def items(self):
        return self.element.find_all(".products dt")

    def item(self, index: int) -> CartMenuItem:
        return CartMenuItem(self.items[index-1])

    def should_have_number_of_items(self, number: int):
        if number > 0:
            self.items.should(have.size(number))
        else:
            raise ValueError("Number should be > 0")
        return self

    @property
    def total_price(self):
        return self.element.find(".ajax_block_cart_total")

    def check_out(self):
        self.element.find("#button_order_cart").click()

    def should_have_only(self, *args: Product):
        self.should_have_number_of_items(len(args))
        for index, product in enumerate(args):
            self.item(index+1).should_have(product)
        return self

    def remove(self, *args: Product):
        raise NotImplementedError
