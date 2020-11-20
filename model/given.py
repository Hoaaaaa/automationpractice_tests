from selene import browser

from model.components.product_list import ProductList


class Given:
    __url = "http://automationpractice.com/"

    @staticmethod
    def at_main_page():
        browser.open_url(Given.__url)

    @staticmethod
    def at_order_page_with_product_in_cart():
        Given.at_main_page()
        ProductList().card(1).add_to_cart()\
            .cart_layer.proceed_to_checkout()
