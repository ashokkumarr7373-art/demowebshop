class BasePage:
    def __init__(self, page):
        self.page = page

    def navigation(self,url):
        self.page.goto(url)

    def click_button(self, locator):
        locator.click()

    def fill_input(self, locator, text):
        locator.fill(text)

    def get_text(self, locator) -> str:
        return locator.text_content()