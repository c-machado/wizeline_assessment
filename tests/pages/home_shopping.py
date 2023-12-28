import logging
from tests.pages.locators import PageLocators

class HomepageShopping:

    def __init__(self, driver):
        self.driver = driver
        self.name = ''
        self.logger = logging.getLogger(__name__)

    def click_on_add_to_cart_cta(self):
        self.name = self.driver.find_element(*PageLocators.item_cart_name).get_attribute('innerHTML')
        self.logger.info(self.name)
        self.driver.click_to_element(PageLocators.add_to_cart_cta)

    def click_on_view_cart_cta(self):
        self.driver.click_to_element(PageLocators.view_cart_cta)


