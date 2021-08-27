

from selenium import webdriver


import unittest

from selenium.webdriver.chrome.options import Options

class ChromeOptionNotificationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Handle chrome Allow block notification
        #1st method
        chrome_options = Options()
        #2nd method
        # chrome_options = webdriver.ChromeOptions()

        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        cls.driver = webdriver.Chrome(executable_path='chromedriver.exe',options=chrome_options)
        cls.driver.maximize_window()





    def testChromeOption(self):
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