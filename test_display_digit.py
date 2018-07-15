# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from numbers import NumberInt
from application import Application


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_display_digit(unittest.TestCase):

    def setUp(self):
        self.app = Application()


    def test_test_display_digit(self):
        self.app.load_home_page()
        self.app.add_one_digit(NumberInt())
        self.app.reset_calc_data()

    def tearDown(self):
        self.app.destroy()

if __name__ == '__main__':
    unittest.main()
