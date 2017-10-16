import unittest

def isOdd(i):
    return True if i%2>0 else False


class TestEvenOrOdd(unittest.TestCase):

    def test_isOdd(self):
        self.assertFalse(isOdd(-2))


unittest.main()