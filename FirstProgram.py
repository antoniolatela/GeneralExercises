import unittest

def isOdd(i):
    return True if i%2>0 else False


class TestEvenOrOdd(unittest.TestCase):

    def test_isOdd(self):
        self.assertTrue(isOdd(1))


unittest.main()