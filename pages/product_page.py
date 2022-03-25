from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.press_the_button(*ProductPageLocators.ADD_TO_BUSKET_BUTTON)
        self.solve_quiz_and_get_code()

    def should_be_message_product_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.MSG_PRODUCT_ADDED_TO_BASKET), "Message that product was added to basket is not presented"

    def should_be_message_basket_with_cost(self):
        assert self.is_element_present(*ProductPageLocators.MSG_BASKET_WITH_COST), "Message with basket cost is not presented"

    def should_be_message_product_name_match(self):
        assert self.get_element_value(*ProductPageLocators.PRODUCT_NAME) == self.get_element_value(*ProductPageLocators.MSG_PRODUCT_NAME), \
            "Product name in message doesn't match product that actually was added"

    def should_be_message_basket_cost_match(self):
        assert self.get_element_value(*ProductPageLocators.PRODUCT_PRICE) == self.get_element_value(*ProductPageLocators.MSG_PRODUCT_PRICE), \
            "Basket cost doesn't match product price that was added"
