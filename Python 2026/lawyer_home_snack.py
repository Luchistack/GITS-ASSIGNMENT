import random


#print("Random Numbers between 1 - 50")
#def random_number():
#
#    for number in range(0, 10):
#
#        numbers = random.randint(1, 50)
#        print(numbers)
#
#random_number()
#print()



print("Random Numbers between 1 - 50")
def random_number(numbers):

    numbers = []

    for number in range(0, 10):

        numbers.append(random.randint(1, 50))
        
    return numbers

print(random_number(10))
print()




def list_number(numbers):
    

    count = 0

    for number in numbers:

        count += 1


    return count

print(f"Numbers in list is:")

print(list_number([1, 2, 3, 4, 5]))
print()



def sum_even_list_number(numbers):
    

    sums = 0

    for index in range(1, len(numbers), 2):
        
        sums += numbers[index] 
    
    return sums

print("Sum of Even indexes is: ")

print(sum_even_list_number([1, 2, 3, 4, 5, 6]))
print()
#
#
#
#
def sum_odd_list_number(numbers):
    

    odd = 0

    for index in range(0, len(numbers), 2):
        
        odd += numbers[index] 
    
    return odd

print("Sum of Odd indexes is: ")

print(sum_odd_list_number([1, 2, 3, 4, 5, 6]))
                           
print()


#

def multiply_third_list_number(numbers):
        
    multiply = 1

    for index in range(2, len(numbers),3):
        
        multiply *= numbers[index] 
    
    return multiply

print("Multiple of third indexes numbers is: ")

print(multiply_third_list_number([3, 4, 2, 1, 4, 8, 7, 8]))

print()
#


def average_of_all_element_in_list(numbers):
    
    average = 0
    sums = 0

    for index in numbers:
        
        sums += index

        average = sums / len(numbers)
    
    return round(average, 2)

print("Average of all element in the list is: ")

print(average_of_all_element_in_list([1, 2, 3, 4, 5, 6, 4]))

print()

#
#
def largest_number(numbers):
    
    numbers.sort()    
         
    return numbers[-1]

print("Largest of all indexes is:")

print(largest_number([1, 2, 15, 3, 4, 5, 6, 4, 11]))

print()



def smallest_number(numbers):

    numbers.sort()    

    return numbers[0]
           
print("smallest number in list is ")


print(smallest_number([2, 1, 15, 3, 4, 5, 6, 4, 11]))
print()
#
#
#9
#def number_string(names):
#
#
#    for name in names:
#
#        if len(name) >= 2 and name[0] == name[-1]:
#
#            return name
#
#
#print(number_string(["anna", "bob", "faith", "joy", "rose"]))
#print()
#
#


#9
#def number_string(names):
#
#
#    return tuple(name for name in names if len(name) >= 2 and name[0] == name[-1])
#
#print("taske nine")
#
#print(number_string(["anna", "bob", "faith", "joy", "rose"]))
#print()
#


#
def sequential(numbers):

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    return numbers


print(sequential([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
print()

#
#
#
def sum_third_list_number(numbers):
        
    total = 0

    for index in range(3, len(numbers),3):
        
        total += numbers[index] 

    return total

print("Sum of third indexes is:")

print(sum_third_list_number([1, 2, 3, 4, 5, 6, 7, 8]))

print()


#

def sum_first_second_third_list_number(numbers):
        
    total = 0

    for index in numbers:
        
        total = numbers[0] + numbers[3] + numbers[-1] 

    return total

print("Sum of First, Second and Third index element is:")

print(sum_third_list_number([1, 2, 3, 5, 6, 7, 8]))

print()



#
