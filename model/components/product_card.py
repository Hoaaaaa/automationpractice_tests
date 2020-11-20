# TODO: consider rename to ProductContainer (element class-like name)
from model.components.layer import Layer


class ProductCard:
    def __init__(self, element):
        self.element = element

    def add_to_cart(self):
        self.element.hover()
        self.element.find(".right-block .ajax_add_to_cart_button").click()
        return Layer()
