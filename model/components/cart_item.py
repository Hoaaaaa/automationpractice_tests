from selene.elements import SeleneElement
from selene.support.conditions import have

from model.components.product import Product


class CartItem:
    def __init__(self, element: SeleneElement):
        self.element = element

    @property
    def name(self):
        return self.element.find(".product-name")

    @property
    def price(self):
        return self.element.find(".cart_unit .price")

    @property
    def total_price(self):
        return self.element.find(".cart_total .price")

    def delete(self):
        self.element.find(".cart_quantity_delete").click()

    def should_have(self, product: Product):
        self.name.should(have.exact_text(f"{product.name}"))
        self.price.should(have.exact_text(f"{product.price}"))
        return self
