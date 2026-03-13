#PSEUDOCODE
#collect three numbers from a user, first number to third number,
#arrange each numbers to be displayed from smallest to largest,
#use the if selection statement to select which is the smallest to the 
#largest number and the number that should be at the middle
#then print out the numbers in ascending order.


first_number = float(input("Enter a number: "))
second_number = float(input("Enter a number: "))
third_number = float(input("Enter a number: "))

if first_number > second_number and first_number > third_number:
	largest = first_number
if second_number > third_number:
    middle = second_number
    smallest = third_number

elif second_number > first_number and second_number > third_number:
	largest = second_number
if first_number > third_number:
    middle = first_number
    smallest = third_number

elif third_number > first_number and third_number > second_number:
	largest = third_number
if first_number > second_number:
    middle = first_number
    smallest = second_number 

print("numbers in ascending order = ", smallest, middle, largest)


