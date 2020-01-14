import unittest
from Password import Password as p

class TestPassword(unittest.TestCase):
    def test_check_complexity(self):
        self.assertTrue(p.check_complexity(True,'1pa55wördd@'))
        self.assertNotEqual(p.check_complexity(False, 'password'), True)
        True

if __name__ == '__main__':
    unittest.main()
