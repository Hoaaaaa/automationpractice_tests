class Product:
    def __init__(self, element):
        self.element = element.find(".right-block")
        # Only visible properties
        self.name = self.element.find(".product-name").text
        self.price = self.element.find(".price").text
        # TODO: not all properties, not all the same exists for each product
