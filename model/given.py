from selene import browser

from model.pages.shop import shop


class Given:
    __url = "http://automationpractice.com/"

    def at_shop(self):
        browser.open_url(self.__url)
        return self

    def at_order_page_with_product_in_cart(self):
        self.at_shop()
        shop.product_list.card(1).add()\
            .cart_layer.proceed_to_checkout()


given: Given = Given()
