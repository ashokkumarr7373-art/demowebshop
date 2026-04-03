from pages.product_page import AddToCartPage


def test_add_to_cart(page,login):

    add_into_cart = AddToCartPage(page)

    add_into_cart.select_category(main_category="Books", sub_category=None)
    add_into_cart.add_to_cart("Computing and Internet")
    add_into_cart.add_to_cart("Fiction")
    add_into_cart.click_cart_icon()
    add_into_cart.click_estimate_shipping()
    add_into_cart.check_agree_checkbox()
    add_into_cart.click_checkout_button()
    title = add_into_cart.get_checkout_title()
    # print(title)
    assert "Checkout" in title, "User is Not able to move to checkout page"


def test_add_to_cart_without_agreeing_terms(page,login):

    add_into_cart = AddToCartPage(page)

    add_into_cart.select_category(main_category="Books", sub_category=None)
    add_into_cart.add_to_cart("Computing and Internet")
    add_into_cart.add_to_cart("Fiction")
    add_into_cart.click_cart_icon()
    add_into_cart.click_estimate_shipping()
    # add_into_cart.check_agree_checkbox()  # Do not check the checkbox
    add_into_cart.click_checkout_button()
    error_message = add_into_cart.get_error_message()
    print(error_message)
    assert "Please accept the terms of service before the next step." in error_message, "Should display error message for not agreeing to terms of service"
    add_into_cart.popup_alert()

















