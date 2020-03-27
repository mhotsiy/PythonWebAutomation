from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from .page import Page
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote import webdriver as WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Remote as RemoteWebDriver


class HomeUserPage(Page):
    driver: WebDriver = None

    def __init__(self, driver: RemoteWebDriver):
        self.driver = driver

    URL = 'https://www.linkedin.com/feed/?trk=guest_homepage-basic_nav-header-signin'

    def page_is_loaded(self):
        wait = WebDriverWait(self.driver, 10)
        page_is_loaded = wait.until(EC.url_to_be(self.URL))
        assert page_is_loaded

