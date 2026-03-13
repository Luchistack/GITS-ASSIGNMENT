item = input("Enter name of item: ")
price = int(input("Enter price of item: "))
code = input("Enter promotional code in CAPITAL LETTER: ")

discount_one= price - 10
discount_two = price / 2

if code == "SAVE10":
        print("You've recieved 10% discount'")
        print("Your payment is: ", discount_one)             
elif code == "HALFOFF":
        print("You've receieved 50% discount")
        print("Your discount payment is: ", discount_two)     
else:
        print('No discount')

