import unittest
import bpm_141

suite = unittest.TestSuite()

suite.addTest(bpm_141.LoginTest("test_admin_login"))
suite.addTest(bpm_141.LoginTest("test_user_login"))

if __name__ =='__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)