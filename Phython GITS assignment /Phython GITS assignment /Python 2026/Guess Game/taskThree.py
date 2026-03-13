import random

guess = int(input("Guess a number: "))
number = random.randint(1, 10)
print(number)


if guess == number:
    print("guessed correctly")

else:
    print(f"Invalid guess | Correct Guess is {number} " )

if guess > number:
    print("Guess is too high")

elif guess < number:
    print("Guess is too low")
