from count_prime import is_prime
import unittest

class TestCount(unittest.TestCase):

    def setUp(self):
        print("test start!")


    def test_case(self):
        self.assertTrue(is_prime(8),msg="is not prime!")


    def tearDown(self):
        print("test end")


if __name__ == '__main__':  #直接使用
    unittest.main()   #执行全部测试用例
#     suite = unittest.TestSuite()
#     suite.addTest(TestCount("test_add2"))
#     runner = unittest.TextTestRunner()
#     runner.run(suite)