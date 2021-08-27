





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
        self.driver.get('https://code.makery.ch/library/dart-drag-and-drop/')
        self.driver.implicitly_wait(5)

        frame = self.driver.find_element_by_xpath("/html/body/div/article/div/div/iframe[1]")

        self.driver.switch_to.frame(frame)

        dragable = self.driver.find_element_by_xpath("(//div[@class='container']/img)[1]")
        self.driver.implicitly_wait(5)
        dropable = self.driver.find_element_by_xpath("//div[@class='container']/div")
        self.driver.implicitly_wait(5)
        ActionChains(self.driver).drag_and_drop(dragable,dropable).perform()

        #switch frame
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath('/html/body/div/nav/ul/li[1]/a').click()



    @classmethod
    def tearDownClass(cls):
        pass
        # cls.driver.close()
        # cls.driver.quit()

if __name__ == '__main__':
    unittest.main()