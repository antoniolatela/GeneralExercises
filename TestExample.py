import unittest
import myprog

class Tests(unittest.TestCase):
    def test_mod_2(self):
        result = myprog.mod_2(2)
        self.assertEqual(0, result)

