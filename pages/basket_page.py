from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_products(self):
        assert self.is_element_present(*BasketPageLocators.ADDED_PRODUCTS), "Product in basket is not presented"

    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.ADDED_PRODUCTS), "Product in basket is presented, but should not be"

    def should_be_message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MSG_BASKET_IS_EMPTY), "Message that basket is empty is not presented"
