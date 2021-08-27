import time
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import HtmlTestRunner

class GoibiboTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        cls.driver.maximize_window()

    def test_homepage(self):
        self.driver.get('https://www.goibibo.com/hotels/')
        self.driver.find_element_by_name('CountryType').click()
        self.driver.implicitly_wait(5)
        # self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/'
        #                                   'section/div[1]/div/div[1]/'
        #                                   'div[1]/input').click()
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/section[1]/'
                                          'div[1]/div/div[3]/div/div[1]/div/div').click()
        self.driver.implicitly_wait(5)

        #check in
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/'
                                          'section[1]/div[1]/div[2]/div[3]'
                                          '/div/div[1]/div[2]/section/div/div[1]'
                                          '/div[2]/div/ul[2]/li[11]/span').click()
        #check out
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/section[1]'
                                          '/div[1]/div[2]/div[3]/'
                                          'div/div[1]/div[2]/section/div/'
                                          'div[1]/div[2]/div/ul[2'
                                          ']/li[13]/span').click()


        #night count
        # print(self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div'
        #                                   '/section[1]/div[1]'
        #                                   '/div[2]/div[3]/div/div[3]').text)
    def test_room(self):

        self.driver.find_element_by_xpath('//input[@class="SearchBlockUIstyles__CitySearchInput-sc-fity7j-12 uGGSH"]').click()
        self.driver.find_element_by_xpath('//input[@class="SearchBlockUIstyles__CitySearchInput-sc-fity7j-12 uGGSH"]').clear()
        #self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/section[1]/div[1]/div[2]/div[4]/div/div/div/div[1]/div/span[2]').click()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test completed')

if __name__ == '__main__':
    unittest.main()

#ele = driver.find_element_by_xpath("//input[@id='downshift-1-input']")

# driver.find_element_by_id('downshift-1-input').click()
# time.sleep(10)
# driver.find_element_by_xpath("//p[text()='Mumbai']").click()




