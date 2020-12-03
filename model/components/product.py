from selene.elements import SeleneElement


class Product:
    def __init__(self, element: SeleneElement):
        self.element = element
        self.name = self.element.find(".product-name").text
        self.price = self.element.find(".right-block .price").text
        self.url = self.element.find(".quick-view")\
            .get_attribute("href")
        # self.image = self.element.find(".product-image-container img")\
        #     .get_attribute("src")
        # self.prod_id = self.element.find(".button-container .ajax_add_to_cart_button")\
        #     .get_attribute("data-id-product")
