from login import Login
import unittest
from selenium import webdriver


class TestCount(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait (4)
        self.browser.get("https://casdev.mioffice.cn/login?service=http://staging.bpm.ad.xiaomi.srv/callback?client_name=CasClient")

    def login_test1(self):
        j = Login('', '')
        j.user_login()

    def login_test2(self):
        j = Login("v-haimingyang","v-haimingyang")
        j.user_login()
        
    # def test_add2(self):
    #     j = Count(41,76)
    #     self.assertAlmostEqual(j.add(),117)

    def tearDown(self):
        print("test end")


if __name__ == '__main__':  #直接使用
    unittest.main()   #执行全部测试用例
#     suite = unittest.TestSuite()
#     suite.addTest(TestCount("test_add2"))
#     runner = unittest.TextTestRunner()
#     runner.run(suite)