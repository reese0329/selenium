
from selenium.webdriver.common.action_chains import ActionChains


class Login():


    def user_login(self, driver):
        driver.find_element_by_id ("miniLogin_username").clear
        driver.find_element_by_id ("miniLogin_username").send_keys ("gumingyu")
        driver.find_element_by_id ("miniLogin_pwd").clear
        driver.find_element_by_id ("miniLogin_pwd").send_keys ("gumingyu")
        driver.find_element_by_id ("message_LOGIN_IMMEDIATELY").click ()


#     def user_logout(self,driver):
# mouse = driver.find_element_by_xpath("//*[@id="dropdown-menu-840"]/li")
# ActionChains(driver).move_to_element(mouse).perform()
# # driver.find_element_by_id("dropdown-menu-4852").click()
# driver.find_element_by_link_text("退出").click()
# driver.quit()