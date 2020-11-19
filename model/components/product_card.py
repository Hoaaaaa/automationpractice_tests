from model.components.product import Product


# TODO: consider rename to ProductContainer (element class-like name)
class ProductCard:
    def __init__(self, element):
        self.element = element

    def add_to_cart(self):
        self.element.hover()
        self.element.find(".right-block .ajax_add_to_cart_button").click()
        # TODO: return cart window

    @property
    def data(self):
        return Product(self.element)
