import unittest
from ch1_6 import string_compress

# Unit test for string compression


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_string_compress(self):
        self.assertEqual(string_compress("aabbbcccc"),"a2b3c4")
        self.assertEqual(string_compress("abc"), "abc")
        self.assertEqual(string_compress("aabbccdd"), "aabbccdd")
        self.assertEqual(string_compress("aaaaa"), "a5")
        self.assertEqual(string_compress("a"), "a")
        self.assertEqual(string_compress(""), "")


if __name__ == '__main__':
    unittest.main(verbosity=2)