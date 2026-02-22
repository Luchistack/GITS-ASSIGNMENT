import random

number = random.randint(1, 10)
total_guess = 1
print(number)


while True:

     guess = int(input("Guess a number: "))

     if guess == number:
        print(f"guess correctly | Correct Guess is {number} " )
        print(f"You won in {total_guess} guess attempt")
        break
     else:
     
        if guess > 10:
            print("Game Over")
            print(f"Correct Guess is {number} " )
            break
        else:
           print("You are wrong, guess again")
            
        total_guess += 1

             
               
