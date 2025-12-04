first_number = int(input("Enter a number: "))
second_number = int(input("Enter a number: "))
third_number = int(input("Enter a number: "))

largest = first_number

if second_number > largest:
    largest = second_number
if third_number > largest:
    largest = third_number

print("Largest =", largest)
