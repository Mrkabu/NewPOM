#  Base on: https://stackoverflow.com/questions/29733636/python-webdriver-attributeerror-loginpage-instance-has-no-attribute-driver

from Locators import Locator


class Start(Locator):

    def __init__(self, driver):
        self.driver = driver
       # self.pobierz()

    #def pobierz(self):
        #self.zalogujElement = self.driver.find_element_by_xpath(self.zaloguj)
        #print(self.zalogujElement)
        #self.terazwtvElement = self.driver.find_element_by_xpath(self.terazwtv)
        #print(self.terazwtvElement)

    def zalogujClick(self):
        self.zalogujElement = self.driver.find_element_by_xpath(self.zaloguj)
        self.zalogujElement.click()
       # self.pobierz()

    def terazwtvClick(self):

        self.terazwtvElement = self.driver.find_element_by_xpath(self.terazwtv)
        self.terazwtvElement.click()
      #  self.pobierz()
