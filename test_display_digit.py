# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_display_digit(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_display_digit(self):
        success = True
        wd = self.wd
        wd.get("http://www.sebuilder.com/")
        wd.get("http://qa-test.klika-tech.com/")
        wd.find_element_by_xpath("//ul[@class='digits']//li[.='1']").click()
        wd.find_element_by_xpath("//ul[@class='operations']//li[.='AC']").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
