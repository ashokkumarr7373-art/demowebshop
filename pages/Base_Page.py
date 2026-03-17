class BasePage:

    def __init__(self,page):
        self.page = page

    def click(self,page):
        click = self.page.click(page)
        return click

