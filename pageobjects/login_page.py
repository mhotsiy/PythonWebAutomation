from selenium.webdriver.support.wait import WebDriverWait
from .page import Page
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote import webdriver as WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Remote as RemoteWebDriver


class LoginPage(Page):
    driver: WebDriver = None

    def __init__(self, driver: RemoteWebDriver):
        super().__init__(driver)
        self.driver = driver

    URL = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
    page_title = 'LinkedIn Login, Sign in | LinkedIn'
    sign_up_button = (By.CSS_SELECTOR, 'button')
    username_field = (By.CSS_SELECTOR, '#username')
    checkbox = (By.XPATH, '//input[@type = "checkbox"]')

    def click_sign_up_button(self):
        button = self.driver.find_element(By.CSS_SELECTOR, "button")
        button.click()

    def enter_username(self, text):
        username = self.driver.find_element(By.CSS_SELECTOR, '#username')
        username.send_keys(text)

    def enter_password(self, text):
        username = self.driver.find_element(By.CSS_SELECTOR, '#password')
        username.send_keys(text)

    def fill_in_credentials(self, user_name, password):
        self.enter_username(user_name)
        self.enter_password(password)

    def checkbox_is_selected(self):
        checkbox = self.driver.find_element(By.XPATH, '//input[@type = "checkbox"]')
        assert checkbox.is_selected()

    def checkbox_is_not_selected(self):
        checkbox = self.driver.find_element(By.XPATH, '//input[@type = "checkbox"]')
        print(checkbox.is_selected())
        assert not checkbox.is_selected()




