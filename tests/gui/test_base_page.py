import allure
from allure_commons.types import AttachmentType
from pytest import mark
from helpers.screenshot import Screenshot
from pageobjects.home_user_page import HomeUserPage
from pageobjects.login_page import LoginPage


@mark.ui
@mark.linkdn
@mark.login_page
class TestBase:
    def test_home_page_title_is_correct(self, browser):
        login_page = LoginPage(browser)
        login_page.open_page()
        assert login_page.get_title == login_page.page_title

    @mark.parametrize(
        'username, password', [
            ('m.hotsiy@gmail.com', 'carlsberg1994')
        ]
    )
    def test_user_can_log_in(self, browser, username, password):
        home_page = LoginPage(browser)
        home_page.open_page()
        home_page.fill_in_credentials(username, password)
        home_page.click_sign_up_button()
        page_cookies = home_page.get_page_cookie()
        home_user_page = HomeUserPage(browser)
        home_user_page.page_is_loaded()
        Screenshot.take_screenshot(browser, 'name')

    @mark.allure
    @mark.checkbox
    def test_checkbox_is_not_selected(self, browser):
        login_page = LoginPage(browser)
        login_page.open_page()
        login_page.checkbox_is_not_selected()
        with allure.step('Making a screenshot'):
            allure.attach(browser.get_screenshot_as_png(),
                          name='Checkbox is not selected',
                          attachment_type=AttachmentType.PNG)

    @mark.xfail(reason='this should fail')
    @mark.checkbox
    def test_checkbox_is_selected(self, browser):
        login_page = LoginPage(browser)
        login_page.open_page()
        login_page.checkbox_is_selected()
        with allure.step('Making a screenshot'):
            allure.attach(browser.get_screenshot_as_png(),
                          name='Checkbox  not selected',
                          attachment_type=AttachmentType.PNG)
