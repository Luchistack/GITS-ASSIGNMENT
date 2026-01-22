import random


number = random.randint(1, 10)
print(number)


while True:
    guess = int(input("Guess a number: "))
    if guess == number:
        print("guessed correctly")
        break
    else:
        print(f"wrong guess | Correct Guess is {number} " )
        
          

