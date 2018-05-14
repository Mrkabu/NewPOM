#  Base on: https://stackoverflow.com/questions/29733636/python-webdriver-attributeerror-loginpage-instance-has-no-attribute-driver

from Locators import Locator

#class LoginPage():
    #zaloguj = '/html/body/header/div/div/div/div/nav/ul/li[2]/a'

class Start(Locator):

    def __init__(self, driver):
        self.driver = driver
        self.zalogujElement = self.driver.find_element_by_xpath(self.zaloguj)


    def userLogin_valid(self):
        self.zalogujElement.click()