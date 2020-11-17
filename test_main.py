from selene.support.conditions import have
from selene.support.jquery_style_selectors import s

from model.app_manager import App
from model.components.product_list import ProductList


def test_user_can_login():
    # TODO: GIVEN user is registered
    App.MainPage.open()
    s(".login").click()
    s("#email").type("hoaa@rambler.ru")
    s("#passwd").type("12345")
    s("#SubmitLogin").click()
    s(".header_user_info .account").should(have.text("Test Test"))


def test_user_can_add_product_to_cart():
    App.MainPage.open()

    product = ProductList().product(1)
    product_name = product.name
    product_price = product.price
    product.add_to_cart()

    s("#layer_cart [title='Proceed to checkout']").click()

    # OrderPage
    s("#order-detail-content .product-name").should(have.text(f"{product_name}"))
    s("#order-detail-content .price").should(have.text(f"{product_price}"))


def test_user_can_delete_product_from_cart():
    # TODO: GIVEN user have product in cart
    App.MainPage.open()
    ProductList().product(1).add_to_cart()
    s("#layer_cart [title='Proceed to checkout']").click()

    # OrderPage
    s("#order-detail-content .cart_quantity_delete").click()
    # TODO: should have 0 products
    s(".alert").should(have.text("Your shopping cart is empty"))
