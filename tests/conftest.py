import playwright
import pytest
from playwright.sync_api import Page, sync_playwright

from pages.Login_Page import LoginPage

@pytest.fixture
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@pytest.fixture
def login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("tharunkumar1293@gmail.com", "123456")
    return login
