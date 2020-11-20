from selene.support.conditions import have
from selene.support.jquery_style_selectors import s

from model.app_manager import App
from model.given import Given
from model.components.product_list import ProductList

# TODO: refactor project structure
# TODO: config pytest output
# TODO: pycharm run/debug don`t use arguments in pytest.ini


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
    # TODO: consider another way to get product
    product = ProductList().product(2).data

    App.MainPage.ProductList.add_to_cart(product)
    # TODO: create window component
    s("#layer_cart [title='Proceed to checkout']").click()

    App.OrderPage.Cart.item(1).should_have(product)


def test_user_can_delete_product_from_cart():
    Given.at_order_page_with_product_in_cart()

    App.OrderPage.Cart.item(1).delete()
    App.OrderPage.should_not_have_cart()
