
import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from tests.consts.constants import Constants

scenarios("../features/shopping_demo.feature")

@given("a user is a the homepage")
def at_the_shopping_homepage(driver, get_web_browser, get_viewport):
    driver.start(get_web_browser, get_viewport)
    driver.go_to_URL(Constants.BASE_URL)


@when("the user clicks on the CTA to add a product")
@given("a user adds a product to the cart")
def add_product_to_the_cart(home_shopping, shopping_cart):
    home_shopping.click_on_add_to_cart_cta()


@given("the user clicks to view the current cart")
def confirm_product_addition(home_shopping, shopping_cart):
    home_shopping.click_on_view_cart_cta()
    assert home_shopping.name == Constants.PRODUCT_NAME
    assert shopping_cart.confirm_item_adittion()


@when("the user enters a valid coupon code")
def enters_valid_coupon(shopping_cart):
    shopping_cart.enters_valid_coupon()


@when("the user clicks on the CTA to apply the coupon")
def clicks_to_apply_coupon(shopping_cart):
    shopping_cart.clicks_to_apply_coupon()


@when("the user clicks to complete the checkout")
def complete_checkout(shopping_cart):
    shopping_cart.clicks_to_checkout()


@when(parsers.parse("the user fills out the user {name}"))
def fills_out_user_details(name, shopping_checkout):
    shopping_checkout.fill_out_user(name)


@then("the system applies the coupon")
def apply_coupon_code(shopping_cart):
    actual_msg = shopping_cart.confirm_coupon_message()
    assert Constants.COUPON_MSG == actual_msg

