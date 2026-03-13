from math import sqrt

#1
name = "rosemary"
for names in name:
    print(f"Reverse string of {name} =", name[::-1], end = " ")
    break
print()


#2
intt = 1234
print(f"Reverse int of {intt} =", str(intt)[::-1])


#6

name = "faith"
for number in name:
    print(ord(number), end = " ")


print()

#7
sums = 0

for numbers in range(1, 101):
    sums += numbers
ave = sums/100
print("Average of 1 - 100 =", ave)
print()

#8
divisor_number = 12
for count in range(1, 13):
    if divisor_number % count == 0:
        print("Numbers divisible by 12 =", count)
print()

#9
divisor_number = 12
counter = 0
for count in range(1, 13):
    if divisor_number % count == 0:
        counter += count
print("Sum of divisible numbers of 12 =", counter)
print()

#10
word = input("Enter a word: ")
if word == word[::-1]:
    print(f"{word} is palindrome")
else:
    print(f"{word} is not a palindrome")
print()


#11
number = (input("Enter a number: "))
if number == number[:: -1]:
        print(f"{number} is palindrome")
else:
    print(f"{number} is not a palindrome")
print()
#12

num = 4 
for nums in range(1):
    print(f"Sqare root of {num} =", sqrt(4))
print()
    
#13
sentence = input("Enter a sentence: ")
words = sentence.split()
counted = len(words)
print("Number of words in the sentence =", counted)
print()


#14
counts = 0
for even_number in range(1,21):
    if even_number % 2 == 0:
        counts += even_number
print("Total of Even numbers =", counts)
print()

#15

counts = 0
for even_number in range(1,21):
    if even_number % 3 == 0:
        counts += even_number
print("Total of odd numbers =", counts)
print()


#16

#17












