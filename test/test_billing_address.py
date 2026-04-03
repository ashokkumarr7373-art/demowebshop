# import time

import allure

from pages.billing_page import BillingPage
from pages.product_page import AddToCartPage
# from playwright.sync_api import expect

def test_billing_address(page,login):


    addtocart = AddToCartPage(page)
    billing = BillingPage(page)

    addtocart.select_category(main_category="Books", sub_category=None)
    addtocart.add_to_cart("Computing and Internet")
    addtocart.add_to_cart("Fiction")
    addtocart.click_cart_icon()
    addtocart.click_estimate_shipping()
    addtocart.check_agree_checkbox()
    addtocart.click_checkout_button()

    try:
        billing.fill_billing_information(
            first_name="John",
            last_name="Doe",
            email="tharun123@gmail.com",
            country="United States",
            city="New York",
            address="123 Main St",
            postal_code="10001",
            phone_number="29276320"
        )

        billing.click_continue_button()
        print("Address added")

    except:
        # fallback → address already exists
        billing.click_continue_button()
        print("Address already exists → continued")

    allure.attach(
        page.screenshot(),
        name="Screenshot",
        attachment_type=allure.attachment_type.PNG
    )



def test_billing_address_with_invalid_data( page, login):

    addtocart = AddToCartPage(page)
    billing = BillingPage(page)

    # Navigate
    addtocart.select_category("Books")
    addtocart.add_to_cart("Computing and Internet")
    addtocart.add_to_cart("Fiction")
    addtocart.click_cart_icon()
    addtocart.click_estimate_shipping()
    addtocart.check_agree_checkbox()
    addtocart.click_checkout_button()

    # Wait for dropdown
    # page.wait_for_selector("#billing-address-select")
    page.wait_for_selector("text=Billing address")

    dropdown = page.locator("#billing-address-select")

    # Get all options
    count = dropdown.locator("option").count()

    if count > 1:
        print("Existing address found → selecting New Address")
        dropdown.select_option(value="")

    else:
        print("No existing address → directly filling")


    page.get_by_label("First name:").wait_for()

    # Fill invalid data
    billing.fill_billing_information(
        first_name="",
        last_name="",
        email="invalid-email",
        country="United States",
        city="New York",
        address="123 Main St",
        postal_code="10001",
        phone_number="29276320"
    )
    allure.attach(
        page.screenshot(),
        name="Screenshot",
        attachment_type=allure.attachment_type.PNG
    )
