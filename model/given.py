from selene import browser

from model.components.product_list import ProductList


__url = "http://automationpractice.com/"


def at_main_page():
    browser.open_url(__url)


def at_order_page_with_product_in_cart():
    at_main_page()
    ProductList().card(1).add_to_cart()\
        .cart_layer.proceed_to_checkout()
