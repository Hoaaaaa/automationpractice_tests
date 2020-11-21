from selene.support.conditions import have
from selene.support.jquery_style_selectors import s

from model import app
from model.given import Given
from model.components.product_list import ProductList

# TODO: refactor project structure
# TODO: config pytest output
# TODO: figure out naming of properties which return class


def test_user_can_login():
    # TODO: GIVEN user is registered
    Given.at_main_page()
    s(".login").click()
    s("#email").type("hoaa@rambler.ru")
    s("#passwd").type("12345")
    s("#SubmitLogin").click()
    s(".header_user_info .account").should(have.text("Tests Test"))


def test_user_can_add_product_to_cart():
    Given.at_main_page()
    product = ProductList().product(2)  # TODO: consider another way to get product

    (app.MainPage
        .ProductList.add_to_cart(product)
        .cart_layer.proceed_to_checkout())

    app.OrderPage.Cart.item(1).should_have(product)


def test_user_can_delete_product_from_cart():
    Given.at_order_page_with_product_in_cart()

    app.OrderPage.Cart.item(1).delete()
    app.OrderPage.should_not_have_cart()
