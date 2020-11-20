class CartLayer:
    def __init__(self, element):
        self.element = element.find(".layer_cart_cart")

    def proceed_to_checkout(self):
        self.element.find(".btn[title='Proceed to checkout']").click()

    def continue_shopping(self):
        self.element.find(".btn.continue").click()
