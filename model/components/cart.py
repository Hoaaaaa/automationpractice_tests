from selene.support.conditions import have
from selene.support.jquery_style_selectors import s

from model.components.cart_item import CartItem


class Cart:
    element = s("table#cart_summary")

    @property
    def items(self):
        return self.element.find_all(".cart_item")

    def item(self, index: int) -> CartItem:
        return CartItem(self.items[index-1])

    def should_have_number_of_items(self, number: int):
        if number > 0:
            self.items.should(have.size(number))
        else:
            raise ValueError("Number should be > 0")
