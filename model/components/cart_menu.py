from selene.elements import SeleneElement
from selene.support.conditions import be, have
from selene.support.jquery_style_selectors import s

from model.components.cart_menu_content import CartMenuContent


class CartMenu:
    element: SeleneElement = s(".header-container .shopping_cart")

    def go_to_cart(self):
        self.element.find("a").click()

    @property
    def quantity(self):
        return self.element.find(".ajax_cart_quantity")

    @property
    def total_price(self):
        return self.element.find(".ajax_cart_total")

    def should_have_quantity(self, quantity: int):
        self.quantity.should(have.exact_text(f"{str(quantity)}"))

    def should_be_empty(self):
        self.element.find(".ajax_cart_no_product").should(be.visible)

    @property
    def content(self) -> CartMenuContent:
        self.element.find("a").hover()
        return CartMenuContent(self.element.find(".cart_block"))
