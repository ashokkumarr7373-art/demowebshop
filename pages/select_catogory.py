# import page

from pages.base_page import BasePage


class SelectCategoryPage(BasePage):

    def __init__(self,page):
        super().__init__(page)
        self.category_selector = page.get_by_role("link", name="Books")
        self.books_title = page.get_by_role("heading", name="Books")
        self.book_title = page.get_by_role("heading", name="Computing and Internet")
        self.add_to_cart_button = page.get_by_role("button", name="Add to cart")
        self.select_product = page.get_by_role("img", name="Picture of Computing and Internet")
        self.input_count = page.locator("#addtocart_13_EnteredQuantity")
        self.compare_product = page.get_by_role("button", name="Add to compare list")
        # self.backToCategory = page.get_by_role("link", name=product)

    def select_category(self,product_name):
        product = self.page.get_by_role("link", name=product_name).first
        product.click()

    def select_products(self,product_name):
        self.page.get_by_role("img", name=product_name)

    def add_to_cart(self, product_name):
        product = self.page.locator(".product-title").filter(has_text=product_name)
        product.self.add_to_cart_button.click()

    def click_the_image(self, product_name):
        # self.page.locator(".product-title").filter(has_text=product_name).click()
        self.page.get_by_alt_text(product_name).click()

    def back_to_category(self, catogory_name):
        self.page.get_by_role("link", name=catogory_name).click()

    def add_to_compare_list(self):
        self.compare_product.click()

    def get_books_title(self):
        return self.books_title.inner_text()

    def get_product_title(self):
        product = self.page.locator(".product-name").text_content()
        return product

    def get_compare_page_title(self):
        title = self.page.locator(".page-title").text_content()
        return title

    def get_book_title(self,name):
        book = self.page.get_by_role("heading", name=name)
        return book.text_content()

    def back_navigation(self):
        self.page.go_back()



    def clear_compare_list(self):
        self.page.get_by_role("link", name="Clear list").click()

    def get_clear_compare_list_message(self):
        message = self.page.get_by_text("You have no items to compare.").text_content()
        return message

    def remove_product(self, product_name):
        column = self.page.locator("td").filter(
            has=self.page.get_by_alt_text(f"Picture of {product_name}")
        )

        with self.page.expect_navigation():
            column.locator("input.remove-button").click()


    def item(self,product_name):
        return self.page.get_by_text(product_name)

    def check(self, product_name):
        return self.page.locator("table").get_by_alt_text(f"Picture of {product_name}")

    def select_sub_category(self, main_category,sub_category):
        product = self.page.get_by_role("link", name=main_category).first
        sub_product = self.page.get_by_role("link", name=sub_category)
        product.hover()
        sub_product.click()


