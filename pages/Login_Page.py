import page
import playwright
from playwright.sync_api import Playwright, sync_playwright, expect

from pages.base_page import BasePage
from tests import conftest


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        # self.page = page

        self.USERNAME_INPUT = page.get_by_role("textbox", name="Email:")
        self.PASSWORD_INPUT = page.get_by_role("textbox", name="Password:")
        self.LOGIN_BUTTON = page.get_by_role("button", name="Log in")

    def login(self, username, password):
        self.fill_input(self.USERNAME_INPUT,username)
        self.fill_input(self.PASSWORD_INPUT,password)
        self.click_button(self.LOGIN_BUTTON)

    def navigate(self):
        base_url = "https://demowebshop.tricentis.com/login"
        self.page.goto(base_url)

    def get_title(self):
        return self.page.title()

    # def login_with_credentials(self, username, password):
    #     browser = playwright.chromium.launch(headless=False)
    #     context = browser.new_context()
    #     page = context.new_page()
    #     page.goto("https://demowebshop.tricentis.com/")
    #     page.get_by_role("link", name="Log in").click()
    #     page.get_by_role("textbox", name="Email:").click()
    #     page.get_by_role("textbox", name="Email:").click()
    #     page.get_by_role("textbox", name="Email:").fill("tharunkumar1293@gmai.com")
    #     page.get_by_role("textbox", name="Password:").click()
    #     page.get_by_role("textbox", name="Password:").fill("123456")
    #     page.get_by_role("checkbox", name="Remember me?").check()
    #     page.get_by_role("button", name="Log in").click()