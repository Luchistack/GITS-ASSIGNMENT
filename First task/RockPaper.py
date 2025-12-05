#collect an input from the user on terminal and call it player1_input
#collect another input from the user an call it player2_input
#check if the input entered by the player is rock or paper or scissors
#check if both inputs are th same and disply TIE if they are
#check if the first input is scissors and the second input is paper then display player1_input wins
#otherwise if vise varsal display player2_input wins
#check if the first input is scissors and the second input is rock then display player2_input wins
#otherwise if vise varsal display player1_input wins
#check if the first input is rock and the second input is paper then display player2_input wins
#otherwise display player1_input wins
#functin is any keword that as  a paratehsis beside it() input(), it displays a message on the terminal and recieves back a message, input takes in a string and returns a string (message)
#the print function takes in anything,, its job is to display things on the terminal print()
#.lower() is only used for string objects, its used to set everycase on the code to lowercase


message =  "Choose a Rock, or paper or scissors:  "

player1_input = input(message)
player2_input = input(message)

if player1_input == player2_input.lower()

    print(TIE)

elif player1_input ==  'scissors' and player2_input == "paper":
    print("player1 wins")

elif player2_input == 'scissors' and player1_input == 'paper':
    print ("player2 wins")

