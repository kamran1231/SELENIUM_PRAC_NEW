






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

    def testDragDrop(self):
        self.driver.get('https://deluxe-menu.com/popup-mode-sample.html')
        self.driver.implicitly_wait(5)

        img = self.driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[2]/div[2]'
                                                '/table[1]/tbody/tr/td[3]/p[2]/img')

        ActionChains(self.driver).context_click(img).perform()
        self.driver.find_element_by_xpath('//*[@id="dm2m1i1tdT"]').click()
        self.driver.find_element_by_xpath('//*[@id="dm2m2i1tdT"]').click()
        self.driver.find_element_by_xpath('//*[@id="dm2m3i1tdT"]').click()



    @classmethod
    def tearDownClass(cls):
        pass
        # cls.driver.close()
        # cls.driver.quit()

if __name__ == '__main__':
    unittest.main()