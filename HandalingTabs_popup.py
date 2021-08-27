




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

        # windows = self.driver.window_handles
        # for window in windows:
        #     print(window)

        self.driver.switch_to.window(self.driver.window_handles[0])

        self.driver.find_element_by_xpath('//*[@id="wrapper"]/header/'
                                          'div[2]/div/div[2]/div/a[1]').click()
        self.driver.implicitly_wait(5)

        #this will handel the window tab
        #1st method
        # windows = self.driver.window_handles
        #
        # for window in windows:
        #     print(window)
        #     self.driver.switch_to.window(window)

        #2nd method
        self.driver.switch_to.window(self.driver.window_handles[1])


        self.driver.find_element_by_xpath('//*[@id="user_email"]').send_keys('khanbrother805@gmail.com')
        self.driver.find_element_by_xpath('//*[@id="user_password"]').send_keys('Iamthebest12')
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input').click()





    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.close()
        #cls.driver.quit()

if __name__ == '__main__':
    unittest.main()