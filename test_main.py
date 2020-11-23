from selene.support.conditions import have
from selene.support.jquery_style_selectors import s

from model import app
from model.given import given
from model.components.product_list import ProductList

# TODO: refactor project structure
# TODO: config pytest output


def test_user_can_login():
    # TODO: GIVEN user is registered
    given.at_main_page()
    s(".login").click()
    s("#email").type("hoaa@rambler.ru")
    s("#passwd").type("12345")
    s("#SubmitLogin").click()
    s(".header_user_info .account").should(have.text("Tests Test"))


def test_user_can_add_product_to_cart():
    given.at_main_page()
    product = ProductList().product(2)

    app.main_page\
        .add_to_cart(product)\
        .cart_layer.proceed_to_checkout()

    app.order_page.cart.item(1).should_have(product)


def test_user_can_delete_product_from_cart():
    given.at_order_page_with_product_in_cart()

    app.order_page.cart.item(1).delete()
    app.order_page.should_not_have_cart()


def test_user_can_add_several_products_to_cart():
    pass
