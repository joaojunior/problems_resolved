import unittest

from hs12mbr import resolve 

class HS12MBR(unittest.TestCase):
    def test_first_example(self):
        self.assertEqual('3 3 3 3', resolve(points=((3, 3))))

if __name__ == '__main__':
    unittest.main()
