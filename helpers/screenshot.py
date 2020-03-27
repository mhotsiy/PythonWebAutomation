from selenium.webdriver import Remote as WebDriver



class Screenshot:

    @staticmethod
    def take_screenshot(driver:WebDriver, name_of_file: str, extension= None, location=None):
        driver.save_screenshot(name_of_file)

