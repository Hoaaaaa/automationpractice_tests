from selene.support.jquery_style_selectors import s

from model.components.product import Product
from model.components.product_card import ProductCard


class ProductList:
    def __init__(self, id_selector: str = ''):
        self.element = s(f".product_list{id_selector}")

    @property
    def products(self):
        return self.element.find_all(".product-container")

    def product(self, index: int) -> Product:
        return Product(self.products[index-1])

    def card(self, index: int) -> ProductCard:
        return ProductCard(self.products[index-1])

    # TODO: temporary solution
    def card_of_(self, product: Product) -> ProductCard:
        return ProductCard(product.element)
