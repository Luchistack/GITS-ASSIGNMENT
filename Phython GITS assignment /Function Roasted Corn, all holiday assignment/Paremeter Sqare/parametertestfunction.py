from parameterfunction import parameter_list
import unittest
class TestParameter(unittest.TestCase):

    def test_square_parameter(self):
            result = parameter_list("2, 3, 4, 5, 7")
            self.assertEqual(result, (4, 9, 16, 25, 49))


if __name__ == "__main__":
        unittest.main()

