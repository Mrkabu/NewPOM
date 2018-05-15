#  from Login import LoginPage
from Login import Start
import unittest
from selenium import webdriver


class Test(unittest.TestCase):

    def test_valid_login(self):
        self.driver = webdriver.Chrome(executable_path=r"E:\Python\Drivery\chromedriver.exe")
        self.driver.get('https://ncplusgo.pl')
        self.driver.maximize_window()
        log_in = Start(self.driver)
        log_in.zalogujClick()

#  W celu zamkniecia przegladarki mozna dodac:

    #  def tearDown(self):
        #  self.driver.quit()

if __name__ == '__main__':
    unittest.main()
