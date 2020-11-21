from selene.support.jquery_style_selectors import s

from model.components.product import Product
from model.components.product_card import ProductCard


class ProductList:
    # TODO: decide return specific by listID or visible condition
    # element = ss(".product_list").find_by(be.visible)

    def __init__(self, id_selector: str = ''):
        self.element = s(f".product_list{id_selector}")

    @property
    def products(self):
        return self.element.find_all(".product-container")

    def product(self, index: int) -> Product:
        return Product(self.products[index-1])

    def card(self, index: int) -> ProductCard:
        return ProductCard(self.products[index-1])

    # TODO: if it don`t need self, is it must be inside ProductList?
    #   MainPage.add_to_cart?
    @staticmethod
    def add_to_cart(product: Product):  # TODO: refactor
        return ProductCard(product.element).add_to_cart()
