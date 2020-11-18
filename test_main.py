from selene.support.conditions import have
from selene.support.jquery_style_selectors import s

from model.app_manager import App
from model.components.product_list import ProductList

# TODO: refactor project structure
# TODO: config pytest output


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

    product = ProductList().product(2)
    # TODO: consider add name, price etc. to init
    product_name = product.name.text
    product_price = product.price.text
    product.add_to_cart()

    s("#layer_cart [title='Proceed to checkout']").click()

    App.OrderPage.Cart.item(1).name.should(have.text(f"{product_name}"))
    App.OrderPage.Cart.item(1).price.should(have.text(f"{product_price}"))


def test_user_can_delete_product_from_cart():
    # TODO: GIVEN user have product in cart
    App.MainPage.open()
    ProductList().product(1).add_to_cart()
    s("#layer_cart [title='Proceed to checkout']").click()

    App.OrderPage.Cart.item(1).delete()
    # App.OrderPage.should_not_have_cart()
    App.OrderPage.Cart.should_have_number_of_items(0)
