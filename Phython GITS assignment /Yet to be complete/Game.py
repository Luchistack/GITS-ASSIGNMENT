
#collect a number from a user
#check if number enter is even 
#use a reminder opertaor %2 == 0 and %2 != 0
#if the number entered is even , diplay even "EVEN", if od, display "ODD"


game_number = int(input("Enter game number: "))

if game_number %2 == 0:
    print("EVEN")
else:
    print ("ODD")
