from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (TimeoutException, NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def press_the_button(self, how, what, timeout=10, is_to_scroll=True):
        try:
            button = WebDriverWait(self.browser, timeout=timeout).until(EC.element_to_be_clickable((how, what)))
            actions = ActionChains(self.browser)

        except TimeoutException as e:
            screenshots_path = f"{what}.jpg"
            self.browser.save_screenshot(screenshots_path)
            raise TimeoutException(f"element {what} didnt appear in {timeout} secs, saving screenshot at "
                                   f"{screenshots_path} which can be found in the junit report")
        if is_to_scroll:
            actions.move_to_element(button).perform()
        actions.click(button).perform()

    def get_element_value(self, how, what, timeout=10, attribute='text'):
        try:
            element = WebDriverWait(self.browser, timeout=timeout).until(EC.presence_of_element_located((how, what)))

            if attribute == 'text':
                return element.text
            else:
                return element.get_attribute(attribute)

        except (TimeoutException, NoSuchElementException):
            return float("NaN")
