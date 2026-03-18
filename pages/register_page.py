from playwright.async_api import Page

from pages.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.register =page.get_by_role("link",name="Register")
        self.gender_male = page.get_by_role("radio",name="Male",exact= True)
        self.gender_female = page.get_by_role("radio",name="Female",exact= True)
        self.first_name = page.get_by_role("textbox",name="FirstName")
        self.last_name = page.get_by_role("textbox",name="LastName")
        self.email = page.get_by_role("textbox",name="Email")
        self.password = page.get_by_role("textbox", name="Password")
        self.confirm_password = page.get_by_role("textbox", name="ConfirmPassword")
        self.error_message = page.locator("field-validation-error")
        self.register_button = page.get_by_role("button", name="Register")
        self.success_message = page.locator(".result")
        # Validation
        self.first_name_error = page.locator("[data-valmsg-for='FirstName']")

    def select_gender(self, gender = "male"):
        if gender.lower() == "male":
            self.gender_male.check()
        else:
            self.gender_female.check()

    def register_click(self):
        self.click_button(self.register)

    def register_page(self,first_name,last_name,email,password,confirm_password):
        self.fill_input(self.first_name, first_name)
        self.fill_input(self.last_name, last_name)
        self.fill_input(self.email, email)
        self.fill_input(self.password, password)
        self.fill_input(self.confirm_password, confirm_password)

    def submit_register(self):
        self.click_button(self.register_button)

    def success_message(self):
        return self.get_text(self.success_message)

    def error_message(self):
        return self.get_text(self.error_message)








