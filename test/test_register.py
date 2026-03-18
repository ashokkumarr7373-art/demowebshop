from pages.register_page import RegisterPage


class TestRegister:

    def test_valid_register(self,page):
        register_page = RegisterPage(page)
        register_page.register_click()
        register_page.select_gender("male")
        register_page.register_page("ashok","kumar", "kumarAshok23@gmail.com", "KumarAshok@123","KumarAshok@123")
        register_page.submit_register()
        register_page.success_message()


    def test_invalid_register(self,page):


