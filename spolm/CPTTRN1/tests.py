import unittest

from cpttrn1 import resolve

class TestCPTTRN1(unittest.TestCase):
    def test_first_example(self):
        self.assertEqual('*\n.\n*', resolve(lines=3, collumns=1))

    def test_seccond_example(self):
        self.assertEqual('*.*.\n.*.*\n*.*.\n.*.*', resolve(lines=4, collumns=4))

    def test_third_example(self):
        self.assertEqual('*.*.*\n.*.*.', resolve(lines=2, collumns=5))

if __name__ == '__main__':
    unittest.main()
