from selene.support.conditions import have


class CartItem:
    def __init__(self, element):
        self.element = element

    @property
    def name(self):
        return self.element.find(".product-name")

    @property
    def price(self):
        return self.element.find(".cart_unit .price")

    @property
    def total_price(self):
        return self.element.find(".cart_total .price")

    def delete(self):
        self.element.find(".cart_quantity_delete").click()

    def should_have(self, product_object):
        # TODO: refactor to using __dir/dict__ etc.
        self.name.should(have.exact_text(f"{product_object.name}"))
        self.price.should(have.exact_text(f"{product_object.price}"))
