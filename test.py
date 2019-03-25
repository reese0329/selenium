from calculator import Count
import unittest

class TestCount(unittest.TestCase):

    def setUp(self):
        print("test start!")


    def test_add(self):
        j = Count(2, 3)
        # self.assertAlmostEqual(j.add(),5)
        j.add()

    def test_add2(self):
        j = Count(41,76)
        # self.assertAlmostEqual(j.add(),117)
        j.add()

    def tearDown(self):
        print("test end")


if __name__ == '__main__':  #直接使用
    unittest.main()   #执行全部测试用例
#     suite = unittest.TestSuite()
#     suite.addTest(TestCount("test_add2"))
#     runner = unittest.TextTestRunner()
#     runner.run(suite)