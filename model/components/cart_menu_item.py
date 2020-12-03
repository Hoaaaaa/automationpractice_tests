from selene.elements import SeleneElement
from selene.support.conditions import have

from model.components.product import Product


class CartMenuItem:
    def __init__(self, element: SeleneElement):
        self.element = element

    @property
    def name(self):
        return self.element.find(".cart_block_product_name")

    @property
    def price(self):
        return self.element.find(".price")

    @property
    def quantity(self):
        return self.element.find(".cart-info .quantity")

    def should_have(self, product: Product):
        self.name.should(have.text(product.name.split()[0]))  # In case of shortened name in menu
        self.price.should(have.exact_text(product.price))
        return self

    def remove(self):
        self.element.find(".remove_link").click()
