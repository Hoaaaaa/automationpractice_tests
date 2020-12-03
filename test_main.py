from selene.support.conditions import have
from selene.support.jquery_style_selectors import s

from model.given import given
from model.components.product_list import ProductList

from model.pages.order import order
from model.pages.shop import shop

# TODO: refactor project structure
# TODO: config pytest output


def test_user_can_login():
    # TODO: GIVEN user is registered
    given.at_shop()
    s(".login").click()
    s("#email").type("hoaa@rambler.ru")
    s("#passwd").type("12345")
    s("#SubmitLogin").click()
    s(".header_user_info .account").should(have.text("Tests Test"))


def test_user_can_add_product_to_cart():
    given.at_shop()
    product = ProductList().product(2)

    shop.product_list.card_of_(product).add()\
        .cart_layer.proceed_to_checkout()

    order.cart_menu.should_have_quantity(1)
    order.cart_menu.content.should_have_only(product)
    order.cart.should_have_only(product)


def test_user_can_delete_product_from_cart():
    given.at_order_page_with_product_in_cart()

    order.cart.item(1).delete()

    order.cart_menu.should_be_empty()
    order.should_not_have_cart()


def test_user_can_add_several_products_to_cart():
    given.at_shop()
    product_one = ProductList().product(3)
    product_two = ProductList().product(4)

    shop.product_list.card_of_(product_one).add()\
        .cart_layer.continue_shopping()

    shop.cart_menu.should_have_quantity(1)
    shop.cart_menu.content.should_have_only(product_one)

    shop.product_list.card_of_(product_two).add()\
        .cart_layer.proceed_to_checkout()

    order.cart_menu.should_have_quantity(2)
    order.cart_menu.content.should_have_only(product_one, product_two)
    order.cart.should_have_only(product_one, product_two)


def test_foo():
    given.at_shop()
    product_one = ProductList().product(3)
    product_two = ProductList().product(4)

    shop.product_list.card_of_(product_one).add() \
        .cart_layer.continue_shopping()

    shop.product_list.card_of_(product_two).add() \
        .cart_layer.proceed_to_checkout()

    order.cart.should_have_only(product_one, product_two)
