


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
        self.driver.implicitly_wait(5)

        slider = self.driver.find_element_by_xpath('/html/body/section[1]/div')
        ActionChains(self.driver).drag_and_drop_by_offset(slider,300,0).perform()



    @classmethod
    def tearDownClass(cls):
        pass
        # cls.driver.close()
        # cls.driver.quit()

if __name__ == '__main__':
    unittest.main()