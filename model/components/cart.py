from selene.support.jquery_style_selectors import s

from model.components.cart_item import CartItem


class Cart:
    element = s("table#cart_summary")

    @property
    def items(self):
        return self.element.find_all(".cart_item")

    def item(self, index):
        return CartItem(self.items[index-1])
