import unittest
from ch1_1 import is_unique1, is_unique2, is_unique3, is_unique4, is_unique5

# Unit test for algorithms to determine if a string has all unique characters.


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_unique_string_char(self):
        self.assertEqual(is_unique1('qwerty asdf'), True)
        self.assertEqual(is_unique1(''), True)
        self.assertEqual(is_unique2('qwerty asdf'), True)
        self.assertEqual(is_unique2(' j'), True)
        self.assertEqual(is_unique3('qwertyasdf'), True) # lower case a-z
        self.assertEqual(is_unique4('qwerty asdf'), True)
        self.assertEqual(is_unique4('&iate1'), True)
        self.assertEqual(is_unique5('qwerty asdf'), True)
        self.assertEqual(is_unique5('0123 ok!456*7$89abc'), True)

    def test_unique_string_char_f(self):
        self.assertEqual(is_unique1('qawertys asdf'), False)
        self.assertEqual(is_unique1('  '), False)
        self.assertEqual(is_unique2('qwertydasdf'), False)
        self.assertEqual(is_unique3('qwertyappsdf'), False)
        self.assertEqual(is_unique4('lqwertyasdfl'), False)
        self.assertEqual(is_unique4('and then it\'s raining'), False)
        self.assertEqual(is_unique5('lqwertyooooasdfl'), False)
        self.assertEqual(is_unique5('0123sgfyga udshg 02'), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)