#SUEDOCODE
#Collect three numbers from a user,
#first_number to third_number
#calculate the sum of all numbers, addition of all numbers,
#the product of all numbers, multiply all numbers together,
#the average of the numbers, the sum of the three numbers divided by 3,
#the largest, display which of the numbers is the smallest
#and smallest of the numbers display which id the smallest 
#and display tota of all, the total, product, average, alrge and small.


first_number = int(input('Enter a number: '))
second_number = int(input('Enter a number: '))
third_number = int(input('Enter a number: '))

total = first_number + second_number + third_number

print("total: ", total)

product = first_number * second_number * third_number

print("product: ", product)

average = total / 3

print("average: ", average)

    largest = first_number

if second_number > largest:
    largest = second_number

if third_number > largest:
    largest = third_number

print("largest: ", largest)

    smallest = first_number

if second_number < smallest:
    smallest = second_number

if third_number < smallest:
    smallest = third_number

print("smallest: ", smallest)


