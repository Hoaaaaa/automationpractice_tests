from selene.elements import SeleneElement


class ProductLayer:
    def __init__(self, element: SeleneElement):
        self.element = element.find(".layer_cart_product")
