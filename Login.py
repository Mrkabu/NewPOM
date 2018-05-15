#  Base on: https://stackoverflow.com/questions/29733636/python-webdriver-attributeerror-loginpage-instance-has-no-attribute-driver

from Locators import Locator


class Start(Locator):

    def __init__(self, driver):
        self.driver = driver
        self.zalogujElement = self.driver.find_element_by_xpath(self.zaloguj)
        self.terazwtvElement = self.driver.find_element_by_css_selector(self.terazwtv)

    def zalogujClick(self):
        self.zalogujElement.click()
        self.terazwtvElement.click()
