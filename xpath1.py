

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class DropdownTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        cls.driver.maximize_window()

    def testXpath(self):
        self.driver.get('http://www.way2automation.com/demo.html')
        self.driver.find_element_by_xpath('//*[@id="toggleNav"]/li[6]/a').click()

        self.driver.implicitly_wait(4)
        xname = self.driver.find_element_by_xpath("//input[@name='name']")
        xname.send_keys('kamran')
        


        # phone = self.driver.find_element_by_xpath("//input[@name='phone']")
        # phone.send_keys('8527075837')
        #
        # email = self.driver.find_element_by_xpath("//input[@name='email']")
        # email.send_keys('khanbrother805@gmail.com')
        #
        # self.driver.find_element_by_xpath("//select[@name='country']").click()



    @classmethod
    def tearDownClass(cls):
        pass
        # cls.driver.close()
        # cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
