#from unittest import TestCase
#class TestClass(TestCase):

 #testcases are method that test different part of the function. every function writting under a class are methods in python.
from palindrome_function_class import word_is_palindrome
import unittest
class TestClass(unittest.TestCase):  

    def test_that_word_is_palindrome(self):

        #self.assertTrue(True)
                Word = madam
                is_palindrome = word_is_palindrome(madam)      
                self.assertTrue(is_palindrome)

