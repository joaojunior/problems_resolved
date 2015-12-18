import unittest

from hs12mbr import resolve 

class HS12MBR(unittest.TestCase):
    def test_first_example(self):
        self.assertEqual('3 3 3 3', resolve(points=[(3, 3)]))

    def test_seccond_example(self):
        self.assertEqual('-10 -10 30 30', resolve(circles=((10, 10, 20), (20, 20, 10))))

    def test_third_example(self):
        self.assertEqual('0 0 100 20', resolve(lines=((0, 0, 100, 20),)))

if __name__ == '__main__':
    unittest.main()
