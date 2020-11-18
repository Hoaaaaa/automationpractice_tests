class ProductCard:
    def __init__(self, element):
        self.element = element
        # TODO: is it right decision?
        self.name = self.element.find(".product-name").text
        self.price = self.element.find(".right-block .product-price").text

    # @property
    # def price(self):
    #     return self.element.find(".right-block .product-price")

    # @property
    # def name(self):
    #     return self.element.find(".product-name")

    def add_to_cart(self):
        self.element.find(".left-block").hover()
        self.element.find(".right-block .ajax_add_to_cart_button").click()
        # TODO: return cart window
