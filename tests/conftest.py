# pylint: disable=import-error, no-name-in-module

from datetime import datetime

import pytest
from py.xml import html

from tests.pages.home_shopping import HomepageShopping
from tests.pages.shopping_cart import Cart
from tests.pages.shopping_checkout import Checkout
from tests.pages.locators import PageLocators
from tests.step_defs.driver import Driver


# print a message with the step in case of error
def pytest_bdd_step_error(
    request, feature, scenario, step, step_func, step_func_args, exception
):
    # print(f'Step failed: {step}', f'Scenario: {scenario}', f'Feature: {feature}')
    print(f'Exception: {exception}')


@pytest.fixture(autouse=True)
def driver():
    # Initialize WebDriver Instance
    driver = Driver()

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit_browser()


@pytest.fixture(scope='session', autouse=True)
def my_cooler_session_finish(request):
    yield
    # you can access the session from the injected 'request':
    session = request.session
    print('session_finish', session)

@pytest.fixture
def home_shopping(driver):
    return HomepageShopping(driver)

@pytest.fixture
def shopping_cart(driver):
    return Cart(driver)

@pytest.fixture
def shopping_checkout(driver):
    return Checkout(driver)


@pytest.fixture
def page_locators(driver):
    return PageLocators()


def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))
    cells.pop()


def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(getattr(report, 'description', '')))
    cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))
    cells.pop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(report, 'duration_formatter', '%H:%M:%S.%f')
    report.description = str(item.function.__doc__)


def pytest_html_report_title(report):
    report.title = 'Wizeline Assessment'
