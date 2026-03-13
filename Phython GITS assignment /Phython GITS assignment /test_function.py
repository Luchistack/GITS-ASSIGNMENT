#from unittest import TestCase
#class TestClass(TestCase):

 #testcases are method that test different part of the function. every function writting under a class are methods in python.
from function_class import number_is_prime
import unittest
class TestClass(unittest.TestCase):  

    def test_that_number_is_prime(self):

        #self.assertTrue(True)
                prime_number = 11
                is_prime = number_is_prime(11)      
                self.assertTrue(is_prime)

    def test_number_is_not_prime(self):

        is_prime = number_is_prime (20)
        self.assertFalse(is_prime)

    def test_if_negative_number_is_prime(self):
            is_prime = number_is_prime(-11)
            self.assertTrue(is_prime)
