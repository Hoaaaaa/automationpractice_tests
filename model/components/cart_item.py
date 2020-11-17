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
