from selene.support.jquery_style_selectors import s

from model.components.layer_cart import CartLayer
from model.components.layer_product import ProductLayer


class Layer:
    element = s("#layer_cart")

    @property
    def cart_layer(self) -> CartLayer:
        return CartLayer(self.element)

    @property
    def product_layer(self) -> ProductLayer:
        return ProductLayer(self.element)

    def close(self):
        self.element.find(".cross[title*='Close']")
