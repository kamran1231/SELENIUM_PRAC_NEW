




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

    def testResize(self):
        self.driver.get('https://jqueryui.com/')
        self.driver.implicitly_wait(5)

        self.driver.find_element_by_xpath('//aside[1]/ul/li[3]/a').click()
        self.driver.implicitly_wait(5)
        resizable = self.driver.find_element_by_xpath("//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
        self.driver.implicitly_wait(5)
        ActionChains(self.driver).drag_and_drop_by_offset(resizable,200,200).perform()



    @classmethod
    def tearDownClass(cls):
        pass
        # cls.driver.close()
        # cls.driver.quit()

if __name__ == '__main__':
    unittest.main()