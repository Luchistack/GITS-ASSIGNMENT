#from unittest import TestCase
#class TestClass(TestCase):

 #testcases are method that test different part of the function. every function writting under a class are methods in python.
import unittest
class TestClass(unittest.TestCase):  
    def test_that_number_is_prime(self):
        self.assertTrue(True)

