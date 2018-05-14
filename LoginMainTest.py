#  from Login import LoginPage
from Login import Start
import unittest
from selenium import webdriver


class GoogleTest(unittest.TestCase):

    def test_valid_login(self):
        self.driver = webdriver.Firefox(executable_path=r"D:\Python\Drivery\geckodriver.exe")
        self.driver.get('https://ncplusgo.pl')
        log_in = Start(self.driver)
        log_in.userLogin_valid()

if __name__ == '__main__':
    unittest.main()
