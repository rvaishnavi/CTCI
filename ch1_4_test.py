import unittest
from ch1_4 import palindrome_perm,palindrome_perm2

# Unit test for URLify


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_palindrome_perm(self):
        self.assertEqual(palindrome_perm("Tact Coa"),True)
        self.assertEqual(palindrome_perm("omm   is si"),True)
        self.assertEqual(palindrome_perm("Aaa Aa"),True )
        self.assertEqual(palindrome_perm("AaaoAa"), False)
        self.assertEqual(palindrome_perm(" oko!  "), False)

    def test_palindrome_perm2(self):
        self.assertEqual(palindrome_perm2("Tact Coa"),True)
        self.assertEqual(palindrome_perm2("omm   is si"),True)
        self.assertEqual(palindrome_perm2("Aaa Aa"),True )
        self.assertEqual(palindrome_perm2("AaaoAa"), False)
        self.assertEqual(palindrome_perm2(" oko!  "), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)