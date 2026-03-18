from playwright.sync_api import expect


class BasePage:
    def __init__(self, page):
        self.page = page

    def navigation(self,url):
        self.page.goto(url)

    def click_button(self, selector):
        self.page.locator.click()

    def fill_input(self, selector, text):
        self.page.locator(selector).fill(text)

    def get_text(self, selector):
        return self.page.locator(selector).text_content()

    def wait_for_visible(self, selector):
        expect(self.page.locator(selector)).to_be_visible()

    def wait_for_url(self, url_part):
        expect(self.page).to_have_url(url_part)

    def take_screenshot(self, name: str):
        self.page.screenshot(path=f"screenshots/{name}.png")

    def get_title(self) -> str:
        return self.page.title()

    