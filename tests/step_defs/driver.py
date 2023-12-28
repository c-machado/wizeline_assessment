import logging
import warnings

import selenium
from selenium import webdriver
from selenium.common import exceptions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.edge.options import Options
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.safari.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

from tests.consts.constants import Constants
from tests.step_defs.i_driver import IDriver

"""IComponent: Methods the component MUST implement" \
 it will derive from the abstract Driver class.
"""


class Driver(IDriver):
    def __init__(self):
        self.driver = None
        self.web_element = None
        self.logger = logging.getLogger(__name__)

    def start(self, web_browser, viewport):
        if web_browser in Constants.UA_BROWSERS:
            self.build_driver_with_user_agent(web_browser, viewport)
        else:
            self.build_driver_for_local(web_browser, viewport)

    def build_driver_for_local(self, web_browser, viewport):
        if web_browser == 'chrome':
            # self.build_chrome_driver(ChromeDriverManager("104.0.5112.20").install(), viewport)
            self.build_chrome_driver(ChromeDriverManager().install(), viewport)
        # elif web_browser == "firefox":
        #     self.build_firefox_driver(GeckoDriverManager().install(), viewport)
        # # elif web_browser == 'safari':
        # #     self.build_safari_driver(viewport)
        # elif web_browser == "edge":
        #     self.build_edge_driver(viewport)
        warnings.filterwarnings(
            action='ignore', message='unclosed', category=ResourceWarning
        )
        return self.driver

    def build_driver_with_user_agent(self, web_browser, viewport):
        for browser_id, ua in Constants.USER_AGENTS.items():
            if browser_id == web_browser:
                print('viewport en main', viewport, web_browser)
                self.set_chrome_ua(ua, viewport)
                warnings.filterwarnings(
                    action='ignore',
                    message='unclosed',
                    category=ResourceWarning,
                )
                return self.driver

    def set_chrome_ua(self, ua, viewport):
        self.build_chrome_driver(ChromeDriverManager().install(), viewport)
        self.driver.execute_cdp_cmd(
            'Network.setUserAgentOverride', {'userAgent': ua}
        )

    def build_chrome_driver(self, driver_path, viewport):
        options = webdriver.ChromeOptions()
        options.add_experimental_option(
            'excludeSwitches', ['enable-automation']
        )
        size_viewport = self.get_window_size(viewport)
        options.add_argument(size_viewport)
        # options.add_argument("user-data-dir=selenium")
        options.set_capability('acceptInsecureCerts', True)
        options.add_argument('--start-maximized')
        # options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        # options.add_argument("--remote-debugging-port=9222")
        # chrome://inspect/#devices
        # options.add_argument(r'--user-data-dir='+Constants.CHROME_PROFILE)  # your chrome user data directory
        # options.add_argument(r'--profile-directory=Person 2')  # the profile with the extensions loaded
        # options.add_argument(r'--profile-directory=Person 1')  # the profile in LINUX
        s = Service(driver_path)
        self.driver = webdriver.Chrome(service=s, options=options)

    def build_edge_driver(self, viewport):
        from selenium.webdriver.edge.options import Options as EdgeOptions

        options = EdgeOptions()
        options.set_capability('acceptInsecureCerts', True)
        # options.add_argument('--headless')
        self.driver = webdriver.Edge(options=options)

    # https://stackoverflow.com/questions/66209119/automation-google-login-with-python-and-selenium-shows-this-browser-or-app-may
    def build_firefox_driver(self, driver_path, viewport):
        self.logger.info('%s build firefox')
        options = Options()
        # options.add_argument('--headless')
        # width = self.get_win_width(viewport, Constants.FF_WINDOWS_WIDTH)
        # height = self.get_win_height(viewport, Constants.FF_WINDOWS_HEIGHT)
        # options.add_argument(width)
        # options.add_argument(height)
        # options.set_preference('profile', Constants.FIREFOX_PROFILE)
        options.add_argument('-profile')
        options.add_argument(Constants.FIREFOX_PROFILE)

        options.set_preference('dom.webdriver.enabled', False)
        options.set_preference('useAutomationExtension', False)

        s = Service(driver_path)
        self.driver = webdriver.Firefox(service=s, options=options)

    # DeprecationWarning: port has been deprecated, please set it via the service class
    def build_safari_driver(self, viewport):
        options = Options()
        # options.set_capability('port', 0)
        # options.add_argument('acceptInsecureCerts=True')
        self.get_win_width(viewport, Constants.SAFARI_WINDOWS_WIDTH)
        self.get_win_height(viewport, Constants.SAFARI_WINDOWS_HEIGHT)
        # options.add_argument(width)
        # options.add_argument(height)
        self.driver = webdriver.Safari(options)
        # self.driver.set_window_size(width, height)

    def refresh(self):
        self.driver.refresh()

    def add_cookie(self, cookie_data):
        self.driver.add_cookie(cookie_data)

    def get_cookie(self, cookie):
        self.driver.get_cookie(cookie)

    def driver_clear(self):
        self.driver.driver_clear()

    def current_url(self):
        return self.driver.current_url

    def click_to_element(self, clickable_element):
        self.wait_for_page_load()
        self.wait_for_element_visible(*clickable_element)
        self.wait_for_element_clickable(*clickable_element)
        self.driver.find_element(*clickable_element).click()

    def close(self):
        self.driver.close()

    def __contains__(self, item):
        return self.driver.__contains__(item)

    def execute_script(self, script):
        return self.driver.execute_script(script)

    def execute_script_locator(self, script, locator):
        return self.driver.execute_script(script, locator)

    def find_element(self, *locator):
        print(locator)
        self.wait_for_element_visible(*locator)
        if locator.__len__() == 2:
            return self.driver.find_element(*locator)
        return self.driver.find_element(*(locator[1], locator[2] % locator[0]))

    def find_elements(self, *locator):
        self.wait_for_all_elements_visible(*locator)
        if locator.__len__() == 2:
            return self.driver.find_elements(*locator)
        return self.driver.find_elements(*(locator[1], locator[2] % locator[0]))

    def get_elements_list(self, locator):
        return self.driver.find_elements(*locator)

    def get_page_source(self):
        return self.driver.page_source

    def go_to_URL(self, url):
        self.driver.get(url)

    def go_back_to_url(self):
        self.driver.back()

    def get_select_options(self, locator):
        options = self.driver.find_element(*locator)
        return Select(options)

    def get_urls_list(self, locator):
        elements = self.driver.find_elements(*locator)
        urls = []
        for element in elements:
            urls.append(element.get_attribute('href'))
        return urls

    @staticmethod
    def get_window_size(viewport):
        for viewport_id, win_size in Constants.CHROME_WINDOWS_SIZE.items():
            if viewport_id == viewport:
                return win_size

    @staticmethod
    def get_win_width(viewport, width_browser):
        for viewport_id, width in width_browser.items():
            if viewport_id == viewport:
                return width

    @staticmethod
    def get_win_height(viewport, height_browser):
        for viewport_id, height in height_browser.items():
            if viewport_id == viewport:
                return height

    def maximize_window(self):
        self.driver.maximize_window()

    def move_to_element(self, to_element):
        from selenium.webdriver.common.action_chains import ActionChains

        action = ActionChains(self.driver)
        # action.move_to_element(to_element).perform()
        action.move_to_element(to_element).release().perform()

    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)

    def switch_to_active_element(self, element):
        self.driver.switch_to.active_element(element)

    def switch_to_active_tab(self):
        handles_before = self.driver.window_handles
        wait = WebDriverWait(self.driver, 50)
        try:
            if handles_before == 1:
                wait.until(lambda x: len(handles_before) > 1)
        except Exception as e:
            print(e)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait_for_page_load()

    def switch_to_iframe(self, element):
        iframe = self.driver.find_element(*element)
        self.driver.switch_to.frame(iframe)

    def quit_browser(self):
        self.driver.quit()

    # TODO: Firefox explicitWait is not working properly
    def wait_for_page_load(self):
        wait = WebDriverWait(self.driver, 20)
        try:
            js_ready = self.execute_script('return document.readyState')
            wait.until(lambda x: js_ready == 'complete')
        except Exception as e:
            self.logger.exception('page does not load')
            print(e)

    def wait_for_feed_to_load(self, *locator):
        wait = WebDriverWait(self.driver, 20)
        try:
            length_list = len(self.driver.find_elements(*locator))
            wait.until(lambda x: length_list > 0)
        except Exception as e:
            self.logger.exception('feed does not load')
            print(e)

    def wait_for_element_clickable(self, *locator):
        wait = WebDriverWait(self.driver, 20)
        try:
            if locator.__len__() == 2:
                return wait.until(
                    expected_conditions.element_to_be_clickable(locator)
                )
        except Exception as e:
            self.logger.exception('element not clickable')
            print(e)

    def wait_for_element_visible(self, *locator):
        wait = WebDriverWait(self.driver, 20)
        try:
            if locator.__len__() == 2:
                return wait.until(
                    expected_conditions.visibility_of_element_located(locator)
                )
        except Exception as e:
            self.logger.exception('element not visible')
            print(e)

    def wait_for_all_elements_visible(self, *locator):
        wait = WebDriverWait(self.driver, 20)
        try:
            if locator.__len__() == 2:
                return wait.until(
                    expected_conditions.visibility_of_all_elements_located(
                        locator
                    )
                )
        except Exception as e:
            self.logger.exception('elements visible')
            print(e)

    def wait_for_element_not_visible(self, *locator):
        wait = WebDriverWait(self.driver, 20)
        try:
            if locator.__len__() == 2:
                return wait.until(
                    expected_conditions.invisibility_of_element_located(locator)
                )
        except Exception as e:
            self.logger.exception('element visible')
            print(e)
