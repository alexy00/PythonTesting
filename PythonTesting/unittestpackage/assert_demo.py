import unittest

class AssertDemo(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a, "a is not True")
        b = False
        self.assertFalse(b, "b is not False")

    def test_assertEqual_1(self):
        a = "Test"
        b = "Test"
        self.assertEqual(a,b,msg="'a' is not Equal to 'b'")


    def test_assertEqual_2(self): # will fail
        a = "Test"
        b = "test"
        self.assertEqual(a,b,msg="'a' is not Equal to 'b'")


    def test_assertNotEqual_1(self):
        a = 10
        b = 20
        self.assertNotEqual(a,b,msg="'a' is Equal to 'b'")

    def test_assertNotEqual_2(self): # will fail
        a = 10
        b = 10
        self.assertNotEqual(a,b,msg="'a' is Equal to 'b'")



if __name__ == '__main__':
    unittest.main(verbosity=2)