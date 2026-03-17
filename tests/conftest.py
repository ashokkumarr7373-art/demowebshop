import playwright
import pytest
from playwright.sync_api import Page


@pytest.fixture(scope="session")
def login_with_credentials(self):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    self.page.goto("https://demowebshop.tricentis.com/")
    self.page.get_by_role("link", name="Log in").click()
    self.page.get_by_role("textbox", name="Email:").click()
    self.page.get_by_role("textbox", name="Email:").click()
    self.page.get_by_role("textbox", name="Email:").fill("tharunkumar1293@gmai.com")
    self.page.get_by_role("textbox", name="Password:").click()
    self.page.get_by_role("textbox", name="Password:").fill("123456")
    self.page.get_by_role("checkbox", name="Remember me?").check()
    self.page.get_by_role("button", name="Log in").click()