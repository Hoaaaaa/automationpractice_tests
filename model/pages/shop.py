from model.components.layer import Layer
from model.components.product import Product
from model.components.product_card import ProductCard
from model.components.product_list import ProductList


class Shop:
    product_list: ProductList = ProductList()

    # TODO: this method not related to main page,
    #   cause don`t try to use ProdList that exists
    #   in Shop instance
    #   Consider refactor through self.ProdList and
    #   ProdList.card(index) -> .card(Product)

    def add_to_cart(self, product: Product) -> Layer:
        card = ProductCard(product.element)
        return card.add_to_cart()


shop: Shop = Shop()
