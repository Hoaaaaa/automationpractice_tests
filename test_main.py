from model.given import given
from model.components.product_list import ProductList

from model.pages.order import order
from model.pages.shop import shop


def test_user_can_add_products_to_cart():
    given.at_shop()
    product_one = ProductList().product(3)
    product_two = ProductList().product(4)

    shop.product_list.card_of_(product_one).add()\
        .cart_layer.continue_shopping()

    shop.cart_menu.should_have_quantity(1)\
                  .should_have_only(product_one)

    shop.product_list.card_of_(product_two).add()\
        .cart_layer.proceed_to_checkout()

    order.cart_menu.should_have_quantity(2)\
                   .should_have_only(product_one, product_two)
    order.cart.should_have_only(product_one, product_two)


def test_user_can_delete_products_in_cart():
    given.at_shop()
    product_one = ProductList().product(3)
    product_two = ProductList().product(4)

    shop.product_list.card_of_(product_one).add() \
        .cart_layer.continue_shopping()

    shop.product_list.card_of_(product_two).add() \
        .cart_layer.proceed_to_checkout()

    order.cart.item(1).delete()

    order.cart_menu.should_have_quantity(1)\
                   .should_have_only(product_two)

    order.cart.item(1).delete()

    order.cart_menu.should_be_empty()
    order.should_not_have_cart()


def test_user_can_delete_products_from_cart_menu():
    given.at_shop()
    product_one = ProductList().product(3)
    product_two = ProductList().product(4)

    shop.product_list.card_of_(product_one).add() \
        .cart_layer.continue_shopping()

    shop.product_list.card_of_(product_two).add() \
        .cart_layer.proceed_to_checkout()

    order.cart_menu.content.item(1).remove()

    order.cart_menu.should_have_quantity(1)\
                   .should_have_only(product_two)

    # TODO: cart and cart_menu have same should methods,
    #  to follow DRY
    order.cart.should_have_only(product_two)

    # TODO: try to make remove by product object,
    #  like cart_menu.remove(product_one)
    #  same for cart
    order.cart_menu.content.item(1).remove()

    order.cart_menu.should_be_empty()
    order.should_not_have_cart()
