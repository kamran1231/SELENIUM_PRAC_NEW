
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import unittest


class MouseMovementTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        cls.driver.maximize_window()

    def testMouseMovement(self):
        self.driver.get('http://www.way2automation.com/')

        menu = self.driver.find_element_by_xpath('//*[@id="navbar-collapse-1"]/ul/li[8]/a')
        action = ActionChains(self.driver)
        action.move_to_element(menu).perform()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//ul/li[8]/ul/li[2]/a').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()