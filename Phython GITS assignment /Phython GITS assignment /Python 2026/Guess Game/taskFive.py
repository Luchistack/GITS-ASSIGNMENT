import random

number = random.randint(1, 10)
total_guess = 1
print(number)


while True:

     guess = int(input("Guess a number: "))

     if guess == number:
        print(f"guess correctly | Correct Guess is {number} " )
        print(f"Total guess is {total_guess}")
        break
     else:
        print("You are wrong, guess again")

        total_guess += 1

         
           
