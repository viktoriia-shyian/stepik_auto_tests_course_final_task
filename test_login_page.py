from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_should_see_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/uk/accounts/login/"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.should_be_login_page()