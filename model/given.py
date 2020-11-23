from selene import browser

from model import app


class Given:
    __url = "http://automationpractice.com/"

    def at_main_page(self):
        browser.open_url(self.__url)
        return self

    def at_order_page_with_product_in_cart(self):
        self.at_main_page()
        app.main_page\
            .product_list.card(1).add_to_cart()\
            .cart_layer.proceed_to_checkout()


given: Given = Given()
