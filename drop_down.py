
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class DropdownTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        cls.driver.maximize_window()

    def testDropdown(self):
        self.driver.get('https://echoecho.com/htmlforms11.htm')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('/html/body/div[2]/'
                                          'table[9]/tbody/tr/td[4]/'
                                          'table/tbody/tr/td/div/span/'
                                          'form/table[1]/tbody/tr/'
                                          'td/table/tbody/'
                                          'tr[2]/td[3]/select').click()

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('/html/body/div[2]/table[9]'
                                          '/tbody/tr/td[4]/table/tbody/tr'
                                          '/td/div/span/form/table[1]'
                                          '/tbody/tr/td/table/tbody/tr[2]'
                                          '/td[3]/select/option[3]').click()
        self.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
