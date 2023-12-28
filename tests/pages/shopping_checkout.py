import time
import logging

from tests.pages.locators import PageLocators

class Checkout:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def fill_out_user(self, name):
        self.logger.info('%s name in example: ', name)
        input_name = self.driver.find_element(*PageLocators.checkout_username)
        input_name.send_keys(name)
        time.sleep(2)
