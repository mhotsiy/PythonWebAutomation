import pytest
from pytest import fixture
from selenium import webdriver
from helpers.test_logger import TestLogger
import time


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='firefox', help="Choose browser: chrome or firefox")


@fixture(scope="function")
def browser(request):
    """Fixture that returns a driver"""
    browser_name = request.config.getoption('browser_name')
    browser = None
    if browser_name == "chrome":
        TestLogger.get_logger().info("start chrome browser for test..")
        browser = webdriver.Chrome()
        browser.implicitly_wait(100)
    elif browser_name == "firefox":
        TestLogger.get_logger().info("start firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()
    TestLogger.get_logger().info('Browser is closed')

