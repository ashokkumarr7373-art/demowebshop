# from playwright.sync_api import expect
class BillingPage:
    def __init__(self,page):
        self.page = page


    def fill_billing_information(self, first_name, last_name, email, country,city, address, postal_code,phone_number):
        self.page.locator("#BillingNewAddress_FirstName").fill(first_name)
        self.page.locator("#BillingNewAddress_LastName").fill(last_name)
        self.page.locator("#BillingNewAddress_Email").fill(email)
        self.page.locator("#BillingNewAddress_CountryId").select_option(label=country)
        self.page.get_by_role("textbox", name="city").fill(city)
        self.page.get_by_role("textbox", name="Address 1:").fill(address)
        self.page.get_by_role("textbox", name="Zip / postal code:").fill(postal_code)
        self.page.get_by_role("textbox", name="Phone number:").fill(phone_number)

    # def dropdown_new(self):
    #     dropdown = self.page.locator("#billing-address-select")
    #
    #     # Get all options
    #     options = dropdown.locator("option")
    #     count = options.count()
    #     return count

    # def handle_billing_address(self):
    #     dropdown = self.page.locator("#billing-address-select")
    #
    #     # Get currently selected value
    #     selected_value = dropdown.input_value()
    #
    #     if selected_value and selected_value.strip() != "":
    #         print("✅ Existing address selected → continuing...")
    #         # Do nothing or click continue
    #         self.page.get_by_role("button", name="Continue").click()
    #
    #     else:
    #         print("➕ No address → selecting New Address and filling form...")
    #
    #         # Select "New Address"
    #         dropdown.select_option(value="")
    #
    #         # Fill form
    #         self.page.get_by_label("First name:").fill("John")
    #         self.page.get_by_label("Last name:").fill("Doe")
    #         self.page.get_by_label("Email:").fill("john@example.com")
    #         self.page.get_by_label("Country:").select_option("India")
    #         self.page.get_by_label("City:").fill("Hyderabad")
    #         self.page.get_by_label("Address 1:").fill("Street 123")
    #         self.page.get_by_label("Zip / postal code:").fill("500001")
    #         self.page.get_by_label("Phone number:").fill("9876543210")
    #
    #         self.page.get_by_role("button", name="Continue").click()
    def click_continue_button(self):
        self.page.get_by_title("Continue").nth(0).click()

    def clear_cookie(self):
        self.page.context.clear_cookies()


