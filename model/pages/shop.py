from selene.support.jquery_style_selectors import s

from model.components.cart_menu import CartMenu
from model.components.layer import Layer
from model.components.product import Product
from model.components.product_list import ProductList


class Shop:
    product_list: ProductList = ProductList()
    layer: Layer = Layer()
    cart_menu: CartMenu = CartMenu()

    # TODO: Current decision don`t use shop.methods,
    #   in order to not create complexity.
    #   Instead only components itself.
    #   Maybe its temp
    def __add_to_cart(self, *args: Product):
        for product in args:
            self.product_list.card_of_(product).add()
            self.layer.cart_layer.continue_shopping()
        return self


shop: Shop = Shop()
