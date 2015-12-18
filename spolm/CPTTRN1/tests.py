import unittest

from cpttrn1 import resolve

class TestCPTTRN1(unittest.TestCase):
    def test_first_example(self):
        self.assertEqual('*\n.\n*', resolve(lines=3, collumns=1))

if __name__ == '__main__':
    unittest.main()
