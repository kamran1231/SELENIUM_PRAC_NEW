

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

from selenium.webdriver.support.select import Select


class DropdownTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        cls.driver.maximize_window()

    def testDropdown(self):
        self.driver.get('https://www.wikipedia.org/')
        self.driver.implicitly_wait(10)
        #One-method
        # self.driver.find_element_by_xpath('//*[@id="searchLanguage"]').click()
        # self.driver.find_element_by_xpath('//*[@id="searchLanguage"]/option[25]').click()

        #Second method
        drop = self.driver.find_element_by_xpath('//*[@id="searchLanguage"]')
        select = Select(drop)
        select.select_by_value('hi')
        self.driver.implicitly_wait(10)

    def testOptionList(self):
        options = self.driver.find_elements_by_xpath("//select[@name='language']//child::option")
        #options = self.driver.find_elements_by_tag_name('option')
        for option in options:
            print('Text is: ',option.text,'Lang is: ',option.get_attribute('lang'))

        print('Total dropdown values are: ',len(options))



    def testLink(self):
        print('Test for all the links present in Website')
        links = self.driver.find_elements_by_tag_name("a")
        for link in links:
            print('-----URL is-----:',link.get_attribute('href'))
        print("Total link of this page:",len(links))



    def testParticleSectionLink(self):
        print('Test link of Specific section')
        pLink = self.driver.find_element_by_xpath('//*[@id="www-wikipedia-org"]/div[7]/div[3]')
        plinks = pLink.find_elements_by_tag_name('a')

        print('1st link is:',pLink.find_elements_by_tag_name('a').__getitem__(0).text)

        for l in plinks:
            print('Url link: ',l.get_attribute('href'))

        print('Length of links is:',len(plinks))



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
