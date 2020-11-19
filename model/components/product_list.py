from selene.support.jquery_style_selectors import s

from model.components.product_card import ProductCard


class ProductList:
    # TODO: decide return specific by listID or visible condition
    # element = ss(".product_list").find_by(be.visible)

    def __init__(self, id_selector=''):
        self.element = s(f".product_list{id_selector}")

    @property
    def products(self):
        return self.element.find_all(".product-container")

    def product(self, index):
        return ProductCard(self.products[index-1])

    def add_product_to_cart(self, index):
        self.product(index).add_to_cart()
