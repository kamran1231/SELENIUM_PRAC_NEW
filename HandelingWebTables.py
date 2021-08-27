




from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import unittest


class TableTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        cls.driver.maximize_window()

    def testTable(self):
        self.driver.get('https://www.espncricinfo.com/series/ipl-2021-1249214/points-table-standings')
        self.driver.implicitly_wait(5)
        rows = self.driver.find_elements_by_xpath('//tbody/tr')
        total_rows = len(rows)

        self.driver.implicitly_wait(5)
        cols = self.driver.find_elements_by_xpath('//tbody/tr[1]/td')
        total_cols = len(cols)
        self.driver.implicitly_wait(5)
        print('Total rows are:',total_rows,'and total cols are:',total_cols)

        for row in rows:
            print(row.text)

        self.driver.implicitly_wait(5)
        print('------Second Way-------')
        start_xpath = "//tbody/tr["
        mid_xpath = "]/td["
        end_xpath = "]"
        self.driver.implicitly_wait(5)
        for row in range(1,total_rows+1):
            for col in range(1,total_cols+1):
                print(self.driver.find_element_by_xpath(start_xpath+str(row)+
                                                        mid_xpath+str(col)+end_xpath).text,end=' ')

    @classmethod
    def tearDownClass(cls):
        
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()