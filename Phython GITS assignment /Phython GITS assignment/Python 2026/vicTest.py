import unittest
from LogisticsFunctions import collection_pay

class Testcollectionpay(unittest.TestCase):

        def test_delivery_above_70 (self):
            self.assertEquals(collection_pay(70), 40000)


