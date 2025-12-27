#ask  three players to choose between "rock", "paper, "scissors"
#display by printing if 'player_1 wins', if 'player_2 wins' and if 'player_3 wins'
#and if its a TIE, using the if and else selection statement
#player_1 = rock and player_2 = scissors,  and player_3 = paper
# we display
# if rock beats scissors, scissors loses to paper, {if rock > scissors and rock < paper, display paper wins}
# if paper beats rock and losses to scissors, scissors wins (if paper > rock and paper < scissors, display scissors wins)
# if scissors beats paper and looses to rock, rock wins (if scissors > paper and scissors < rock, display rock wins)
# else display TIE


#player_1 = input("Player 1, Choose a player (Rock, Paper or Scissors): ")
#player_2 = input("Player 2, Choose a player (Rock, Paper or Scissors): ")
#player_3 = input("Player 3, Choose a player (Rock, Paper or Scissors): ")

#winner = player_1 

#if player_2 > winner:
    # winner = player_2
#if player_3 > winner:
   #  winner = player_3
    #print("winner =", winner)
#else:
   # print("TIE")

choose = "Choose a player (Rock, Paper or Scissors:  "

player_1 = input("choice of player: ")

player_2 = input("choice of player: ")



if player_1 == player_2:
    print("TIE")

elif player_1 == 'scissors' and player_2 == 'paper':
    print("player_1 WINS")

elif player_2 == 'scissors' and player_1 == 'paper':
    print("player_2 WINS")





