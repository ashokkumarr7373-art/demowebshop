import playwright
import pytest
from playwright.sync_api import sync_playwright

from test.conftest import login
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


@pytest.mark.parametrize("username, password", [("tharunkumar1293@gmail.com", "1293456"),
                                                               ("tharunkumar1293@gmail.com", "wrong_password"),
                                                               ("wronge_user@gmail.com","123456"),
                                                               ("","123456"),
                                                               ("tharunkumar1293@gmail.com",""),
                                                               ("","")])
def test_invalid_login(page, username, password):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(username, password)
    message = login_page.error_message()
    assert "Login was unsuccessful." in message, f"Expected error message, got: {message}"







