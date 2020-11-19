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

    # TODO: if it dont need self, is it must be inside ProductList?
    @staticmethod
    def add_to_cart(product):
        ProductCard(product.element).add_to_cart()
