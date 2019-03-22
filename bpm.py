# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from public import Login


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://casdev.mioffice.cn/login?service=http://staging.bpm.ad.xiaomi.srv/callback?client_name=CasClient")
driver.maximize_window()

Login().user_login(driver)
# logout()
driver.quit()
