


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import unittest


class WindowTabTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.headless = True
        cls.driver = webdriver.Chrome(executable_path='chromedriver.exe',options=chrome_options)
        cls.driver.maximize_window()

    def testScreeshot(self):
        self.driver.get('https://way2automation.com/')
        S = lambda X : self.driver.execute_script('return document.body.parentNode.scroll'+ X)
        self.driver.set_window_size(S('Width'),S('Height'))
        self.driver.find_element_by_tag_name('body').screenshot('./screenshot/fullpage.jpg')



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        #cls.driver.quit()

if __name__ == '__main__':
    unittest.main()