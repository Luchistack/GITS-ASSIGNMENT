#from unittest import TestCase
#class TestClass(TestCase):

from Discountfuntionclass import check_code
import unittest
class TestDiscount(unittest.TestCase):  

    def test_save10_discount(self):
        result = check_code(100, "SAVE10")
        self.assertEqual(result, 90.0)

    def test_save50_discount(self):
        result = check_code(100, "HALFOFF")
        self.assertEqual(result, 50.0)

    def test_no_discount(self):
        result = check_code(100, "INVALID")
        self.assertEqual(result, 100.0)

if __name__ == "__main__":
        unittest.main()

