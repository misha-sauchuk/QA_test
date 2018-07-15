# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from numbers import NumberInt


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_display_digit(unittest.TestCase):

    def setUp(self):
        self.wd = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
        self.wd.implicitly_wait(5)
    
    def test_test_display_digit(self):
        self.load_home_page()
        self.add_one_digit(NumberInt())
        self.reset_calc_data()

    def reset_calc_data(self):
        wd = self.wd
        wd.find_element_by_xpath("//ul[@class='operations']//li[.='AC']").click()

    def add_one_digit(self, number):
        wd = self.wd
        path = "//ul[@class='digits']//li[.='{}']".format(number.digit)
        wd.find_element_by_xpath().click()

    def load_home_page(self):
        wd = self.wd
        wd.get("http://qa-test.klika-tech.com/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
