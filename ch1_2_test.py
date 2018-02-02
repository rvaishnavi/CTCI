import unittest
from ch1_2 import is_perm1, is_perm2

# Unit test for methods to decide if one string is a permutation of the other


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_one_string_permutation_of_other(self):
        self.assertEqual(is_perm1('god','dog'), True)
        self.assertEqual(is_perm1('123aa34bb!     ', ' aabb   ! 12334'), True)
        self.assertEqual(is_perm1('', ''), True)
        self.assertEqual(is_perm1(' space*2', '2 *apsce'), True)
        self.assertEqual(is_perm2('god', 'dog'), True)
        self.assertEqual(is_perm2('how are you', 'yeor  wohau'), True)
        self.assertEqual(is_perm2('!78  yo yo 91', 'ooyy1789!    '), True)
        self.assertEqual(is_perm2('that\'s ok', '\'thatok s'), True)

    def test_one_string_permutation_of_other_f(self):
        self.assertEqual(is_perm1('God', 'dog'), False)
        self.assertEqual(is_perm1('GgOo', 'ggoo'), False)
        self.assertEqual(is_perm1('', ' '), False)
        self.assertEqual(is_perm2('God', 'dog'), False)
        self.assertEqual(is_perm2('that\'s ok', '\'that ok '), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)