
from semicolonfunction import length_of_string
import unittest
class Test_semicolon(unittest.TestCase):

    def  test_semicolon_length(self):
        result = length_of_string("semicolon")
        self.assertEqual(9)

    if __name__ == "__main__":
        unittest.main()
