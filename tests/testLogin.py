import playwright
from playwright.sync_api import sync_playwright

from tests.conftest import login_with_credentials


def test_valid_login(page):
    # login = login_with_credentials()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demowebshop.tricentis.com/")
    page.get_by_role("link", name="Log in").click()
    page.get_by_role("textbox", name="Email:").click()
    page.get_by_role("textbox", name="Email:").click()
    page.get_by_role("textbox", name="Email:").fill("tharunkumar1293@gmai.com")
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill("123456")
    page.get_by_role("checkbox", name="Remember me?").check()
    login = page.get_by_role("button", name="Log in").click()
    print(login.get_title())
