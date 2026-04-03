# import pytest
from playwright.sync_api import expect

# from test import conftest
from pages.select_catogory import SelectCategoryPage

class TestProducts:

    def test_products(self,login):
        click_category = SelectCategoryPage(login)
        click_category.select_category("Apparel & Shoes")
        title = click_category.get_compare_page_title()

        assert "Apparel & Shoes" in title, "Should navigate to Apparel & Shoes category page"

    def test_click_image(self,login):
        product = "50's Rockabilly Polka Dot Top JR Plus Size"
        click_image = SelectCategoryPage(login)
        click_image.select_category("Apparel & Shoes")
        # click_image.select_category()
        click_image.click_the_image(product)
        title = click_image.get_product_title()
        assert product in title, f"Should navigate to product page for {product}"

    # @pytest.mark.parametrize("prod1", [("50's Rockabilly Polka Dot Top JR Plus Size", "Blue Jeans")])
    def test_compare_products(self,login):
        product1 = "50's Rockabilly Polka Dot Top JR Plus Size"
        product2 = "Blue Jeans"
        compare = SelectCategoryPage(login)
        compare.select_category("Apparel & Shoes")
        compare.click_the_image(product1)
        compare.add_to_compare_list()
        compare.back_navigation()
        compare.select_category("Apparel & Shoes")
        compare.click_the_image(product2)


        compare.add_to_compare_list()


        # title = compare.get_comapare_page_title()
        # assert  "Compare products" in title, "Should navigate to compare products page"
        expect(compare.check(product1)).to_be_visible()
        expect(compare.check(product2)).to_be_visible()
        # expect(compare.item(prod1)).to_be_visible()
        # expect(compare.item(product2)).to_be_visible()





    def test_clear_all_compare_list(self,login):
        text = "You have no items to compare."
        clear = SelectCategoryPage(login)
        clear.select_category("Apparel & Shoes")
        clear.click_the_image("50's Rockabilly Polka Dot Top JR Plus Size")
        clear.add_to_compare_list()
        clear.clear_compare_list()
        message = clear.get_clear_compare_list_message()
        assert text in message, "Compare list should be cleared and show appropriate message"

    def test_remove_from_compare_list(self,login):
        product1 = "50's Rockabilly Polka Dot Top JR Plus Size"
        product2 = "Blue Jeans"
        remove = SelectCategoryPage(login)
        remove.select_category("Apparel & Shoes")
        remove.click_the_image(product1)
        remove.add_to_compare_list()
        remove.back_navigation()
        remove.select_category("Apparel & Shoes")
        remove.click_the_image(product2)
        remove.add_to_compare_list()
        remove.remove_product(product1)
        # expect(self.page.get_by_text("50's Rockabilly Polka Dot Top JR Plus Size")).not_to_be_visible()
        expect(remove.item(product1)).not_to_be_visible()


    def test_add_to_cart_from_compare_list_with_multiple_count(self,login):
        # product = ""
        compare = SelectCategoryPage(login)
        # compare.select_category("Computers")
        compare.select_sub_category("Computers","Notebooks")
        compare.click_the_image("14.1-inch Laptop")
        compare.add_to_compare_list()
        compare.select_sub_category("Computers","Desktops")
        compare.click_the_image("Build your own computer")
        compare.add_to_compare_list()
        expect(compare.check("14.1-inch Laptop")).to_be_visible()
        expect(compare.check("Build your own computer")).to_be_visible()






