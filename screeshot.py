






from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import unittest


class WindowTabTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        cls.driver.maximize_window()

    def testWindowTab(self):
        self.driver.get('https://way2automation.com/')
        #self.driver.save_screenshot("./screenshot/error.jpg")
        ele = self.driver.find_element_by_xpath('//*[@id="wrapper"]/header/div[2]/div/div[1]/a/img')
        ele.screenshot('./screenshot/ele.jpg')






    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

        #cls.driver.quit()

if __name__ == '__main__':
    unittest.main()