from selene import browser
from selene.support.conditions import have
from selene.support.jquery_style_selectors import s

from model.components.product_card import ProductCard


def test_user_can_login():
    browser.open_url("http://automationpractice.com/")
    s(".login").click()
    s("#email").type("hoaa@rambler.ru")
    s("#passwd").type("12345")
    s("#SubmitLogin").click()
    s(".header_user_info .account").should(have.text("Test Test"))


def test_user_can_add_product_to_cart():
    browser.open_url("http://automationpractice.com/")
    product = ProductCard()
    product.add_to_cart()
    s("#layer_cart [title='Proceed to checkout']").click()
    s("#order-detail-content .product-name").should(have.text(f"{product.name}"))
    s("#order-detail-content .price").should(have.text(f"{product.price}"))


def test_user_can_delete_product_from_cart():
    # TODO: GIVEN user have product in cart
    browser.open_url("http://automationpractice.com/")
    product = ProductCard()
    product.add_to_cart()
    s("#layer_cart [title='Proceed to checkout']").click()
    s("#order-detail-content .cart_quantity_delete").click()
    # TODO: should have 0 products
    s(".alert").should(have.text("Your shopping cart is empty"))
