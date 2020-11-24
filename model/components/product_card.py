# TODO: consider rename to ProductContainer (element class-like name)
from model.components.layer import Layer


class ProductCard:
    def __init__(self, element):
        self.element = element

    def add(self) -> Layer:
        self.element.hover()
        self.element.find(".right-block .ajax_add_to_cart_button").click()
        return Layer()

    # TODO: is it place for product -> Product()?
    #   cause Product().element locate inside ProductCard.element
