import playwright
from playwright.sync_api import Playwright, sync_playwright, expect
class LoginPage:

    def __init__(self, page):
        self.page = page

    import re
    # from playwright.sync_api import Playwright, sync_playwright, expect
    #
    # def run(playwright: Playwright) -> None:
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
    #     page.get_by_role("textbox", name="Email:").click()
    #     page.get_by_role("textbox", name="Email:").click()
    #     page.get_by_role("textbox", name="Email:").press("ArrowRight")
    #     page.get_by_role("textbox", name="Email:").fill("tharunkumar193@gmai.com")
    #     page.get_by_role("textbox", name="Email:").press("ArrowRight")
    #     page.get_by_role("textbox", name="Email:").fill("tharunkumar123@gmai.com")
    #     page.get_by_role("textbox", name="Email:").press("ArrowRight")
    #     page.get_by_role("textbox", name="Email:").fill("tharunkumar1239@gmai.com")
    #     page.get_by_role("textbox", name="Password:").click()
    #     page.get_by_role("textbox", name="Password:").click()
    #     page.get_by_role("textbox", name="Password:").fill("123456")
    #     page.get_by_role("button", name="Log in").click()
    #     page.get_by_role("textbox", name="Email:").click()
    #     page.get_by_role("textbox", name="Email:").press("ArrowRight")
    #     page.get_by_role("textbox", name="Email:").press("ArrowRight")
    #     page.get_by_role("textbox", name="Email:").press("ArrowRight")
    #     page.get_by_role("textbox", name="Email:").fill("tharunkumar123@gmai.com")
    #     page.get_by_role("button", name="Log in").click()
    #     page.get_by_role("textbox", name="Password:").click()
    #     page.get_by_role("textbox", name="Password:").fill("123456")
    #     page.get_by_role("button", name="Log in").click()
    #     page.locator("form").filter(has_text="Login was unsuccessful.").click()
    #     page.get_by_role("textbox", name="Email:").click()
    #     page.get_by_role("textbox", name="Email:").press("ControlOrMeta+a")
    #     page.get_by_role("textbox", name="Email:").fill("tharunkumar1293@gmail.com")
    #     page.get_by_role("textbox", name="Password:").click()
    #     page.get_by_role("textbox", name="Password:").fill("123456")
    #     page.get_by_role("button", name="Log in").click()
    #
    #     # ---------------------
    #     context.close()
    #     browser.close()
    #
    # with sync_playwright() as playwright:
    #     run(playwright)
    def login(self, username, password):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    def navigate(self):
        base_url = config["BASE_URL"]
        self.page.goto(base_url)

    def login_with_credentials(self, username, password):
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
        page.get_by_role("button", name="Log in").click()