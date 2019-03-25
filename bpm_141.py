# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from public_141 import Login
import time

class LoginTest(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://casdev.mioffice.cn/login?service=http://staging.bpm.ad.xiaomi.srv/callback?client_name=CasClient")
        self.driver.maximize_window()


    def test_admin_login(self):
        username = "gumingyu"
        password = "gumingyu"
        Login().user_login(self.driver, username, password)


    def test_user_login(self):
        username = "v-haimingyang"
        password = username
        Login().user_login(self.driver, username, password)

    def tearDown(self):
        print("test end!")


# Login().user_login(driver)
# # logout()
# driver.quit()
#
# LoginTest().test_admin_login()
# time.sleep(3)
# LoginTest().test_user_login()
# time.sleep(3)

if __name__ == '__main__':
    unittest.main()