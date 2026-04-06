import allure
import pytest
from playwright.sync_api import expect
from pages.select_catogory import SelectCategoryPage


@allure.feature("Product Comparison")
class TestProducts:

    @allure.title("Navigate to Apparel & Shoes Category")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("User can navigate to a product category")
    def test_products(self, login):
        with allure.step("Initialize Category Page"):
            click_category = SelectCategoryPage(login)

        with allure.step("Select 'Apparel & Shoes' category"):
            click_category.select_category("Apparel & Shoes")
            allure.attach(
                login.screenshot(),
                name="Apparel & Shoes Category Page",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Get page title and verify"):
            title = click_category.get_compare_page_title()
            allure.attach(
                f"Page title: {title}",
                name="Page Title",
                attachment_type=allure.attachment_type.TEXT
            )
            assert "Apparel & Shoes" in title, \
                "Should navigate to Apparel & Shoes category page"

    # ──────────────────────────────────────────────────────

    @allure.title("Click Product Image and Verify Product Page")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("User can click a product image and land on product page")
    def test_click_image(self, login):
        product = "50's Rockabilly Polka Dot Top JR Plus Size"

        with allure.step("Initialize Category Page"):
            click_image = SelectCategoryPage(login)

        with allure.step("Select 'Apparel & Shoes' category"):
            click_image.select_category("Apparel & Shoes")
            allure.attach(
                login.screenshot(),
                name="Category Page",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step(f"Click on product image: {product}"):
            click_image.click_the_image(product)
            allure.attach(
                login.screenshot(),
                name="Product Page After Click",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Verify product page title"):
            title = click_image.get_product_title()
            allure.attach(
                f"Product title: {title}",
                name="Product Title",
                attachment_type=allure.attachment_type.TEXT
            )
            assert product in title, \
                f"Should navigate to product page for {product}"

    # ──────────────────────────────────────────────────────

    @allure.title("Compare Two Products in Apparel & Shoes")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("User can add two products to compare list and verify both appear")
    def test_compare_products(self, login):
        product1 = "50's Rockabilly Polka Dot Top JR Plus Size"
        product2 = "Blue Jeans"

        with allure.step("Initialize Category Page"):
            compare = SelectCategoryPage(login)

        with allure.step("Select 'Apparel & Shoes' and open first product"):
            compare.select_category("Apparel & Shoes")
            compare.click_the_image(product1)
            allure.attach(
                login.screenshot(),
                name=f"Product 1 Page - {product1}",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step(f"Add '{product1}' to compare list"):
            compare.add_to_compare_list()
            allure.attach(
                login.screenshot(),
                name="After Adding Product 1 to Compare",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Navigate back and open second product"):
            compare.back_navigation()
            compare.select_category("Apparel & Shoes")
            compare.click_the_image(product2)
            allure.attach(
                login.screenshot(),
                name=f"Product 2 Page - {product2}",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step(f"Add '{product2}' to compare list"):
            compare.add_to_compare_list()
            allure.attach(
                login.screenshot(),
                name="After Adding Product 2 to Compare",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Verify both products are visible in compare list"):
            allure.attach(
                login.screenshot(),
                name="Compare List with Both Products",
                attachment_type=allure.attachment_type.PNG
            )
            expect(compare.check(product1)).to_be_visible()
            expect(compare.check(product2)).to_be_visible()

    # ──────────────────────────────────────────────────────

    @allure.title("Clear All Items from Compare List")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("User can clear the entire compare list")
    def test_clear_all_compare_list(self, login):
        text = "You have no items to compare."

        with allure.step("Initialize Category Page"):
            clear = SelectCategoryPage(login)

        with allure.step("Select category and open product"):
            clear.select_category("Apparel & Shoes")
            clear.click_the_image("50's Rockabilly Polka Dot Top JR Plus Size")
            allure.attach(
                login.screenshot(),
                name="Product Page",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Add product to compare list"):
            clear.add_to_compare_list()
            allure.attach(
                login.screenshot(),
                name="Product Added to Compare List",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Clear the entire compare list"):
            clear.clear_compare_list()
            allure.attach(
                login.screenshot(),
                name="After Clearing Compare List",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Verify empty compare list message"):
            message = clear.get_clear_compare_list_message()
            allure.attach(
                f"Message shown: {message}",
                name="Empty Compare List Message",
                attachment_type=allure.attachment_type.TEXT
            )
            assert text in message, \
                "Compare list should be cleared and show appropriate message"

    # ──────────────────────────────────────────────────────

    @allure.title("Remove One Product from Compare List")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("User can remove a specific product from compare list")
    def test_remove_from_compare_list(self, login):
        product1 = "50's Rockabilly Polka Dot Top JR Plus Size"
        product2 = "Blue Jeans"

        with allure.step("Initialize Category Page"):
            remove = SelectCategoryPage(login)

        with allure.step("Add first product to compare list"):
            remove.select_category("Apparel & Shoes")
            remove.click_the_image(product1)
            remove.add_to_compare_list()
            allure.attach(
                login.screenshot(),
                name=f"Added {product1} to Compare",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Add second product to compare list"):
            remove.back_navigation()
            remove.select_category("Apparel & Shoes")
            remove.click_the_image(product2)
            remove.add_to_compare_list()
            allure.attach(
                login.screenshot(),
                name=f"Added {product2} to Compare",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step(f"Remove '{product1}' from compare list"):
            remove.remove_product(product1)
            allure.attach(
                login.screenshot(),
                name=f"After Removing {product1}",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step(f"Verify '{product1}' is no longer visible"):
            allure.attach(
                login.screenshot(),
                name="Final Compare List State",
                attachment_type=allure.attachment_type.PNG
            )
            expect(remove.item(product1)).not_to_be_visible()

    # ──────────────────────────────────────────────────────

    @allure.title("Add Products from Different Categories to Compare List")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("User can compare products from different sub-categories")
    def test_add_to_cart_from_compare_list_with_multiple_count(self, login):

        with allure.step("Initialize Category Page"):
            compare = SelectCategoryPage(login)

        with allure.step("Navigate to Computers > Notebooks and open product"):
            compare.select_sub_category("Computers", "Notebooks")
            compare.click_the_image("14.1-inch Laptop")
            allure.attach(
                login.screenshot(),
                name="14.1-inch Laptop Page",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Add '14.1-inch Laptop' to compare list"):
            compare.add_to_compare_list()
            allure.attach(
                login.screenshot(),
                name="Laptop Added to Compare",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Navigate to Computers > Desktops and open product"):
            compare.select_sub_category("Computers", "Desktops")
            compare.click_the_image("Build your own computer")
            allure.attach(
                login.screenshot(),
                name="Build Your Own Computer Page",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Add 'Build your own computer' to compare list"):
            compare.add_to_compare_list()
            allure.attach(
                login.screenshot(),
                name="Desktop Added to Compare",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Verify both products appear in compare list"):
            allure.attach(
                login.screenshot(),
                name="Final Compare List - Both Products",
                attachment_type=allure.attachment_type.PNG
            )
            expect(compare.check("14.1-inch Laptop")).to_be_visible()
            expect(compare.check("Build your own computer")).to_be_visible()