import random

def taskOne():

    number = random.randint(1, 10)
    print(number)


def taskTwo():

    guess = int(input("Guess a number: "))
    number = random.randint(1, 10)
    print(number)

    if guess == number:
        print("guessed correctly")

    else:
        print(f"Wrong guess | Correct Guess is {number} " )


def taskThree():

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


def taskFour():

    guess = int(input("Guess a number: "))
    number = random.randint(1, 20)
    print(number)


    while True:

        if guess == number:
            print("guessed correctly")
            break
        else:
            print(f"wrong guess | Correct Guess is {number} " )

          


def taskFive():

    total_guess = 1
    number = random.randint(1, 20)
    print(number)


    while True:
        
        guess = int(input("Guess a number: "))
        if guess == number:
            print("guessed correctly")
            print("Total guess is {total_guess}")
            break
        else:
            print(f"wrong guess | Correct Guess is {number} " )

            total_guess += 1

            exit()

def
           



def main():

    taskOne()
#
    taskTwo()

    taskThree()
    
    taskFour()

    taskFive()
main()
