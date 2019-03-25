import unittest
import bpm_141
from HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()

suite.addTest(bpm_141.LoginTest("test_admin_login"))
suite.addTest(bpm_141.LoginTest("test_user_login"))

if __name__ =='__main__':
    runner = unittest.TextTestRunner()


    #定义报告存放路径
    fp = open('.result.html','wb')
    runner = HTMLTestRunner(stream=fp, title = 'bpm', description ='用例执行情况')
    runner.run (suite)
    fp.close()