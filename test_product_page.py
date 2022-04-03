import pytest
import random
import string

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # should be api creation
        self.browser = browser
        self.link = "http://selenium1py.pythonanywhere.com/uk/accounts/login/"
        min_for_password_char_num = 9
        email = ''.join(random.choice(string.ascii_letters) for _ in range(min_for_password_char_num)) + "@gmail.com"
        password = ''.join(random.choice(string.ascii_letters) for _ in range(min_for_password_char_num))

        # usually do not do browser manipulation, here only for setup usage practice
        login_page = LoginPage(self.browser, self.link)
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

        self.link = "http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/"

        # yield
        # should be data delete

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):
        page = ProductPage(self.browser, self.link)
        page.open()
        page.add_product_to_basket()
        page.should_be_success_message()
        page.should_be_message_product_name_match()
        page.should_be_message_basket_with_cost()
        page.should_be_message_basket_cost_match()

    def test_user_cant_see_success_message(self):
        page = ProductPage(self.browser, self.link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_success_message()
    page.should_be_message_product_name_match()
    page.should_be_message_basket_with_cost()
    page.should_be_message_basket_cost_match()


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"])
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"])
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products()
    basket_page.should_be_message_basket_is_empty()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"])
def test_guest_should_see_login_link_on_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.xfail
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_disappear_success_message()
