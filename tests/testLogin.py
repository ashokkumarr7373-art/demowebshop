from tests.conftest import login_with_credentials


def test_valid_login(login_with_credentials):
    login = login_with_credentials()
    print(login.get_title())
