from selenium import webdriver
import unittest
import time

class Login():

    def __init__(self, username, password):
        self.username = username
        self.password = password
        # self.driver = webdriver.Chrome

    # def setUp(self):
    #     self.driver = webdriver.Chrome()
    #     self.base_url = "https://casdev.mioffice.cn/login?service=http://staging.bpm.ad.xiaomi.srv/callback?client_name=CasClient"
    #     self.driver.implicitly_wait(4)

    def user_login(self):
        driver = self.driver
        driver.get(self.base_url+"/")
        driver.find_element_by_id ("miniLogin_username").clear
        driver.find_element_by_id ("miniLogin_username").send_keys (self.username)
        driver.find_element_by_id ("miniLogin_pwd").clear
        driver.find_element_by_id ("miniLogin_pwd").send_keys (self.password)
        driver.find_element_by_id ("message_LOGIN_IMMEDIATELY").click ()
        time.sleep(3)
    #
    # def tearDown(self):
    #     self.driver.quit()
#
# if __name__ == "__main__":
#     unittest.main()

