import playwright
from playwright.sync_api import sync_playwright

from tests.conftest import login
from pages.Login_Page import LoginPage


def test_valid_login(page):
    # print("Login successful")
    # login = login_with_credentials()
    login_page = LoginPage(page)
    #
    login_page.navigate()
    login_page.login("tharunkumar1293@gmail.com", "123456")
    login_page.get_title()


def test_invaid(login):
    print("Login successful")
    login.get_title()




