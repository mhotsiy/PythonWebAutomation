from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Remote as RemoteWebDriver

from selenium.webdriver.support.wait import WebDriverWait


class Page:
    URL = None

    def __init__(self, driver: RemoteWebDriver):
        self.driver = driver

    def find_element(self, locator, time=10) -> RemoteWebDriver:
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def open_page(self):
        return self.driver.get(self.URL)

    @property
    def get_title(self):
        return self.driver.title

    def get_page_cookie(self):
        return self.driver.get_cookies()

