# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from public import Login


class LoginTest(object):

    def __int__(self, driver):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://casdev.mioffice.cn/login?service=http://staging.bpm.ad.xiaomi.srv/callback?client_name=CasClient")
        self.driver.maximize_window()

    def test_admin_login(self):
        username = "gumingyu"
        password = "gumingyu"
        Login().user_login(self.driver, username, password)
        self.driver.quit()

    def test_user_login(self):
        username = "v-haimingyang"
        password = username
        Login().user_login(self.driver, username, password)
        self.driver.quit()



# Login().user_login(driver)
# # logout()
# driver.quit()

LoginTest().test_admin_login()
LoginTest().test_user_login()