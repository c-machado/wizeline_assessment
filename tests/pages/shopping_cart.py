import logging
from tests.consts.constants import Constants
from tests.pages.locators import PageLocators

class Cart:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def enters_valid_coupon(self):
        coupon_field = self.driver.find_element(*PageLocators.coupon_code_field)
        coupon_field.send_keys(Constants.COUPON_CODE)

    def clicks_to_apply_coupon(self):
        self.driver.click_to_element(PageLocators.coupon_code_cta)

    def clicks_to_checkout(self):
        self.driver.click_to_element(PageLocators.checkout_cta)

    def confirm_item_adittion(self):
        return self.driver.find_element(*PageLocators.cart_item)

    def confirm_coupon_message(self):
        msg = self.driver.find_element(*PageLocators.coupon_code_confirmation_msg).get_attribute('innerHTML')
        self.logger.info(msg.strip())
        return msg.strip()
