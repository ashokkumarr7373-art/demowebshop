from playwright.sync_api import expect


class BasePage:
    def __init__(self, page):
        self.page = page

    def navigation(self,url):
        self.page.goto(url)

    def click_button(self, locator):
        self.page.locator.click()

    def fill_input(self, locator, text):
        self.page.locator.fill(text)

    def get_text(self, locator):
        return self.page.locator.text_content()

    def wait_for_visible(self, locator):
        expect(self.page.locator).to_be_visible()

    def wait_for_url(self, url_part):
        expect(self.page).to_have_url(url_part)

    def take_screenshot(self, name: str):
        self.page.screenshot(path=f"screenshots/{name}.png")

    def get_title(self) -> str:
        return self.page.title()

    