for numbers in range(1, 101):
    if numbers %2 == 0:
        print(numbers)


for odd in range(50, 101):
    if odd % 3 == 0:
        print(odd, end = " ")

for reverse in range(101, 0, -1):
    print(reverse)

for square in range(1, 22):
    tot = square * square
    print(tot, end = " ")

for multiples in range(1, 51, 3):
        print(multiples)

for num in range(1, 101):
    if num %3 == 0 and num %5 == 0:
        print(num, end = " ")

count = 0
for numb in range(1, 101):
    if numb % 7 == 0:
        count += 1       
print("Total count =", count)


sums = 0
for natural in range(1, 51):
    sums += natural
print("Sum of first natural number =", sums)


multiple = 1
for product in range(1, 11):
    multiple *= product
print("Product of 10 natural number =", multiple)


for letters in range(97, 123):
    print(chr(letters), end = " ")

times = 5
time = 0
for count in range(1, 13):
    time = times * count
    result = f"{times} X {count} = "
    print(result, time)

name = "faith"
for let in name:
    print(let) 



e = "letter"
count = 0
for howmany_e in e:
    if howmany_e == "e":
        count += 1
print("E in string =", count)
    




words = " "
for letters in words:
    words = "miracle"
    print(words.upper())



word = " "
for uppercase in word:
    word = "miracle"
    print(word.lower())





string ="Angela" 
count = 0 
for vowel_letters in string:
    if vowel_letters.lower() in "aeiou":
        count += 1  
print("Vowel in string =", count) 




score = 123456
count = 0
for given_number in str(score):
    count += 1
print("total number in digit =", count)
    



sums = 0
score = 123456
count = 0
for given_number in str(score):
    count += 1
    sums += count
print("total sum in digit =", sums)



    
maximum = 0
score = 123456
for scores in str(score):
    scores = int(scores)
    if scores > maximum:
        maximum = scores
print("larget in digit =", maximum)



   
minimum = 9
score = 236456
for scores in str(score):
    scores = int(scores)
    if scores < minimum:
        minimum = scores
print("smallest in digit =", minimum)

