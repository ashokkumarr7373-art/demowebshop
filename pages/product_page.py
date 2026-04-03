class AddToCartPage:

    def __init__(self, page):
        self.page = page

    def back_navigation(self):
        self.page.go_back()

    def select_category(self, main_category, sub_category=None):
        main = self.page.locator(".top-menu").get_by_role("link", name=main_category)

        if sub_category:
            main.first.hover()
            self.page.locator(".top-menu") \
                .get_by_role("link", name=sub_category) \
                .first.click()
        else:
            main.first.click()


    def add_in_to_cart(self, product_name):
        self.page.get_by_text("Build your own cheap computer").click()

        self.page.locator("input[id^='add-to-cart-button']").click()
        # self.page.locator("input[id^='add-to-cart-button']")

    def add_to_cart(self,product_name):
        product = self.page.locator(".product-item").filter(
            has=self.page.get_by_role("link", name=product_name)
        )

        product.locator(".product-box-add-to-cart-button").click()
    def get_cart_count(self):
        text = self.page.locator(".cart-qty").inner_text()  # "(2)"
        return text

    def click_cart_icon(self):
        # cart click
        self.page.get_by_text("Shopping cart").nth(0).click()

    def click_estimate_shipping(self):
        self.page.get_by_role("button", name="Estimate shipping").click()

        # cart count

    def check_agree_checkbox(self):
        self.page.locator("input[name='termsofservice']").check()

    def click_checkout_button(self):
        self.page.get_by_role("button", name="Checkout").click()

    def get_checkout_title(self):
        title = self.page.locator(".page-title").text_content()
        return title

    def get_error_message(self):
        warning = self.page.locator("#terms-of-service-warning-box").text_content()
        return warning

    def popup_alert(self):
        self.page.on("dialog", lambda dialog: dialog.dismiss())
        # self.page.get_by_role("button").click()





