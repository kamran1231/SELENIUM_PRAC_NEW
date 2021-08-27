


from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import unittest


class AlertTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        cls.driver.maximize_window()

    def testAlert(self):
        self.driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
        self.driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/form/'
                        'div[1]/div[2]/div[2]/div[2]/input[2]').click()
        self.driver.implicitly_wait(5)

        #1st method
        #alert = Alert(self.driver)

        #2nd method
        alert = self.driver.switch_to.alert
        self.driver.implicitly_wait(10)
        print(alert.text)
        alert.accept()



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()