import playwright
import pytest
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
    welcome = login_page.assert_login()
    assert "Welcome to our store" in welcome
    # login_page.get_title()
    # assert


@pytest.mark.parametrize("username, password", [("tharunkumar1293@gmail.com", "123456"),
                                                               ("tharunkumar1293@gmail.com", "wrong_password"),
                                                               ("wrong_user","123456"),
                                                               ("","123456"),
                                                               ("tharunkumar1293@gmail.com",""),
                                                               ("","")])
def test_invalid_login(page, username, password, error_message):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(username, password)
    messege = login_page.error_message()
    assert "Login was unsuccessful. Please correct the errors and try again" not in messege, f"Expected error message, got: {messege}"

def test_printt(page):
    login_page = LoginPage(page)
    #
    login_page.navigate()
    login_page.login("tharunkumar1293@gmail.com", "")

    print(login_page.error_message)





