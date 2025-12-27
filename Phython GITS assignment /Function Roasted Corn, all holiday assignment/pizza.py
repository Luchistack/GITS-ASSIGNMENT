#WElcome to iya Scambirah pizza joint Ajegunle
#collect customer order
#dispplay available pizza and cost and quantity
#what type of pizza do you want to buy (pizza type = odugwu)
#How many people are you looking at....at least one slice for each guest of 45, (NUmber of people = 45)
#How many boxes of pizza would you love to buy (4 boxes)
#How many total slice in the total number of packs (enough for 45 people), each contains 12 slice per box, total of 4 boxes is 48
#Display how many will be leftover slice  after all guest have been served
#How much the customer has to pay for it, bill is(prices = 16800)( 4200 per box for 4 boxes))


total = 0

print("\nWELCOME TO IYA SCAMBIRAH PIZZA JOINT Ajegunle!")

print("\n==============================================")
print("\tHere are The Pizzas avaiable")
print("\t============================")

print("\n 1.Supa size\n 2.Small Money\n 3.Big Boys\n 4.Odugwu\n")

pizza = input("what type of pizza do you want to buy: ").lower().strip()
print("==========================")
print(f"you just selected {pizza}")
print("==========================")

if pizza == "supa size":
    price = 2000
    print(f"A box of supa size pizza cost {price}")

elif pizza == "small money":
   price = 2000
   print(f"A box of small money pizza cost {price}")

elif pizza == "big boys":
    price = 3600
    print(f"A box of big boys pizza cost {price}")

elif pizza == "odugwu":
    price = 4200
    print(f"A box of odugwu pizza cost {price}")

guest = int(input("\nHow many guest are you looking at: "))
print("========================")
print(f"Number of guest = {guest}")
print("========================")
boxes = int(input("\nHow many boxes of pizza would you like to buy: "))
print("=============================")
print(f"Boxes of pizza selected is {boxes}")
print("=======================================")
total_slice = 12 * boxes
print(f"Total slices of pizzas in {boxes} boxes are {total_slice}")
left_over = total_slice - guest
print(f"\nThere will be {left_over} left over pizzas after all guest have been served")



if pizza in ["odugwu" or "small money" or "big boys" or "supa size"]:
    total = boxes * price
print(f"\nTotal cost of {boxes} boxes of pizza is {total}")
print(f"Your bill is {total}")





