import unittest
from ch1_5 import oneeditaway

# Unit test for oneeditaway


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_one_edit_away(self):
        self.assertEqual(oneeditaway("apple","aple"),True)
        self.assertEqual(oneeditaway("pale","apale"), True)
        self.assertEqual(oneeditaway("pale", "tale"), True)
        self.assertEqual(oneeditaway("hole", "holy"), True)
        self.assertEqual(oneeditaway("pale", "pale"), True)
        self.assertEqual(oneeditaway("india", "in"), False)
        self.assertEqual(oneeditaway("india","indiain"), False)
        self.assertEqual(oneeditaway("sanjose", "monjose"), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)