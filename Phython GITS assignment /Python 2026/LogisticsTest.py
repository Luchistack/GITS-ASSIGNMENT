import unittest
from LogisticsFunctions import collection_pay

class TestCollectionPay(unittest.TestCase):

    def test_70_and_above(self):
        self.assertEqual(collection_pay(70), 40000)

    def test_60_to_69(self):
        self.assertEqual(collection_pay(65), 21250)

    def test_50_to_59(self):
        self.assertEqual(collection_pay(55), 16000) 

    def test_below_50(self):
        self.assertEqual(collection_pay(40), 11400)
