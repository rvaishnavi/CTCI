import unittest
from ch1_3 import urlify,urlify2

# Unit test for URLify


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_urlify_of_a_string(self):
        self.assertEqual(urlify("Mr John Smith    ",13), "Mr%20John%20Smith")
        self.assertEqual(urlify("a b  ",3), "a%20b")
        self.assertEqual(urlify("", 0), "")

    def test_urlify_of_a_string2(self):
        self.assertEqual(urlify2("Mr John Smith    ",13), "Mr%20John%20Smith")


if __name__ == '__main__':
    unittest.main(verbosity=2)