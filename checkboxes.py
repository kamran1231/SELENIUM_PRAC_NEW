

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class DropdownTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        cls.driver.maximize_window()


    def testCheckBoxes(self):

        self.driver.get('http://www.tizag.com/htmlT/htmlcheckboxes.php')

        #One method to select indiviual
        # self.driver.find_element_by_xpath('//div[4]/input[1]').click()
        #
        # self.driver.find_element(By.XPATH,'//div[4]/input[2]').click()
        #
        # self.driver.find_element_by_xpath('//div[4]/input[3]').click()
        #
        # self.driver.find_element_by_xpath('//div[4]/input[4]').click()

        #Second method for click the checkbox for using for loop
        self.driver.implicitly_wait(5)
        checkboxes = self.driver.find_elements(By.NAME,'sports')
        print(len(checkboxes))
        for checkbox in checkboxes:
            print('Before clicking: ',checkbox.is_selected())
            checkbox.click()
            print('After clicking: ',checkbox.is_selected())


        self.driver.implicitly_wait(5)




    @classmethod
    def tearDownClass(cls):
        pass
        # cls.driver.close()
        # cls.driver.quit()





if __name__ == '__main__':
    unittest.main()
