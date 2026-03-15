import random

from unittest import TestCase

import lawyer_home_snack

class test_lawyer_home_snack(TestCase):

    def test_that_a_list_of_ten_random_numbers_is_created(self):

        numbers = [] 

        actualResult = lawyer_home_snack.random_number(numbers)

        expectedResult = 10

        self.assertEqual(expectedResult, len(actualResult))


    def test_total_numbers_in_list(self):

        numbers = [1, 2, 3, 4, 5]

        actualResult = lawyer_home_snack.list_number(numbers)

        expectedResult = 5

        self.assertEqual(expectedResult, actualResult)


    def test_sum_of_total_even_numbers_in_the_list(self):

        numbers = [1, 2, 3, 4, 5, 6]

        actualResult = lawyer_home_snack.sum_even_list_number(numbers)

        expectedResult = 12

        self.assertEqual(expectedResult, actualResult)


    def test_sum_of_total_odd_numbers_in_the_list(self):

        numbers = [1, 2, 3, 4, 5, 6]

        actualResult = lawyer_home_snack.sum_odd_list_number(numbers)

        expectedResult = 9

        self.assertEqual(expectedResult, actualResult)


    def test_multiplication_of_total_third_numbers_in_the_list(self):

        numbers = [3, 4, 2, 1, 4, 8, 7, 8]

        actualResult = lawyer_home_snack.multiply_third_list_number(numbers)

        expectedResult = 16

        self.assertEqual(expectedResult, actualResult)



    def test_total_average_of_all_element_in_list(self):

        numbers = [1, 2, 3, 4, 5, 6, 4]

        actualResult = lawyer_home_snack.average_of_all_element_in_list(numbers)

        expectedResult = 3.57

        self.assertEqual(expectedResult, actualResult)







    def test_largest_number_in_the_list(self):

            
        numbers = [2, 1, 15, 3, 4, 5, 6, 4, 11]

        actualResult = lawyer_home_snack.largest_number(numbers)

        expectedResult = 15

        self.assertEqual(expectedResult, actualResult)





    def test_smallest_number_in_the_list(self):

            
        numbers = [2, 1, 15, 3, 4, 5, 6, 4, 11]

        actualResult = lawyer_home_snack.smallest_number(numbers)

        expectedResult = 1

        self.assertEqual(expectedResult, actualResult)

#
#    def test_number_of_string(self):
#
#            
#        names = ["anna", "bob", "faith", "joy", "rose"]
#
#        actualResult = lawyer_home_snack.number_string(names)
#
#        expectedResult = ('anna', 'bob')
#
#        self.assertEqual(expectedResult, actualResult)


    def test_sequential_number_in_the_list(self):

            
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

        actualResult = lawyer_home_snack.sequential(numbers)

        expectedResult = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

        self.assertEqual(expectedResult, actualResult)



    def test_sum_of_third_number_in_the_list(self):

            
        numbers = [1, 2, 3, 4, 5, 6, 7, 8]

        actualResult = lawyer_home_snack.sum_third_list_number(numbers)

        expectedResult = 11

        self.assertEqual(expectedResult, actualResult)


    def test_the_sum_first_second_third_list_number(self):

            
        numbers = [1, 2, 3, 4, 5, 6, 7, 8]

        actualResult = lawyer_home_snack.sum_first_second_third_list_number(numbers)

        expectedResult = 13

        self.assertEqual(expectedResult, actualResult)

