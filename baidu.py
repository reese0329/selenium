#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
#鼠标悬停在搜索设置按钮上
mouse = driver.find_element_by_class_name("setting-text")
ActionChains(driver).move_to_element(mouse).perform()
