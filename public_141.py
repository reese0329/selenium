

class Login():


    def user_login(self, driver,username,password):
        driver.find_element_by_id ("miniLogin_username").clear
        driver.find_element_by_id ("miniLogin_username").send_keys(username)
        driver.find_element_by_id ("miniLogin_pwd").clear
        driver.find_element_by_id ("miniLogin_pwd").send_keys(password)
        driver.find_element_by_id ("message_LOGIN_IMMEDIATELY").click()