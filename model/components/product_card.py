from selene.support.jquery_style_selectors import s


class ProductCard:
    card = s(".product-container")

    def __init__(self):
        self.name = self.card.find(".product-name").text
        self.price = self.card.find(".right-block .product-price").text

    def add_to_cart(self):
        self.card.find(".left-block").hover()
        self.card.find(".right-block .ajax_add_to_cart_button").click()
