#WElcome to iya Scambirah pizza joint Ajegunle
#collect customer order
#display available pizza and cost and quantity
#what type of pizza do you want to buy (pizza type = odugwu) ----- cntr + shift u, 20a6 to get ₦ sign
#How many people are you looking at....at least one slice for each guest of 45, (NUmber of people = 45)
#How many boxes of pizza would you love to buy (4 boxes)
#How many total slice in the total number of packs (enough for 45 people), each contains 12 slice per box, total of 4 boxes is 48
#Display how many will be leftover slice  after all guest have been served
#How much the customer has to pay for it, bill is(prices = 16800)( 4200 per box for 4 boxes))


#PIZZAS PRICE INITIALIZATION
supa_price = 2000
small_price = 3000
big_boys_price = 3600
odugwu_price = 4200 

#PIZZAS SLICES INITIALIZAION
supa_size_slices = 4
small_money_slices = 5
big_boys_slices = 8
odugwu_slices = 12


def menu():
        #Multiline string to print multiple strings
        print( """ \nWELCOME TO IYA SCAMBIRAH PIZZA JOINT Ajegunle!

        ==========================================
        Here are The list of Pizzas avaiable below
        ==========================================

        1. Supa size @ ₦2000
        2. Small Money @ ₦3000
        3. Big Boys @ ₦3600
        4. Odugwu @ ₦4200
        5. Quit

        Select from the available options or enter 5 to quit
        """)


menu()

selected_pizza_type = input("what type of pizza do you want to buy: ").lower()

def details(selected_pizza_type):
    match selected_pizza_type:
        case "1":
            print("======================================")
            print(f"you just selected {selected_pizza_type} @ Supa size pizza")
            print(f"Supa size pizza costs ₦{supa_price}")
            print("============================")

        case "2":
            print("=======================================")
            print(f"you just selected {selected_pizza_type} @ Small Money pizza")
            print(f"Small money pizza costs ₦{small_price}")
            print("============================")


        case "3":
            print("=======================================")
            print(f"you just selected {selected_pizza_type} @ Big Boys pizza")
            print(f"Big boys pizza costs ₦{big_boys_price}")
            print("=============================")

        case "4":
            print("=======================================")
            print(f"you just selected {selected_pizza_type} @ Odugwu pizza")
            print(f"Odogwu pizza costs ₦{odugwu_price}")
            print("=============================")


        case "5": 
            print("Thank you for shopping with us")
            exit()
                

        case _:
                print("Invalid pizza selection!")
                exit()


details(selected_pizza_type)


guest = int(input("\nHow many guest are you looking at: "))
print("=============================")
print(f"Number of guest is {guest}")
print("=============================")

boxes = int(input("\nHow many boxes of pizza would you like to buy: "))
print("=============================")
print(f"Boxes of pizza selected is {boxes}")
print("=============================")


def pizza_type(selected_pizza_type):

    match selected_pizza_type:
        case "1":
            cost = supa_price * boxes
            total_slices = supa_size_slices * boxes
            total = supa_price * boxes
            left_over = total_slices - guest
            print(f"You've selected Supa size pizza, costs ₦{supa_price}")
            print(f"\nTotal cost of {boxes} boxes of pizza is {total}")
            print("===================")
            print(f"Your bill is {total}")
            print("===================")
            
            print(f"Total slices of pizzas in {boxes} boxes are {total_slices}")
            print(f"\nThere will be {left_over} left over pizzas after all guest have been served a pizza each")
     

        case "2":
            cost = small_price * boxes
            total_slices = small_money_slices * boxes
            total = small_price * boxes
            left_over = total_slices - guest
            print(f"You've selected Small money pizza, costs ₦{small_price}")
            print(f"\nTotal cost of {boxes} boxes of pizza is ₦{total}")
            print("===================")
            print(f"Your bill is ₦{total}")
            print("===================")
            print(f"Total slices of pizzas in {boxes} boxes are {total_slices}")
            print(f"\nThere will be {left_over} left over pizzas after all guest have been served a pizza each")

        case "3":
            cost = big_boys_price * boxes
            total_slices = big_boys_slices * boxes
            total = big_boys_price * boxes
            left_over = total_slices - guest
            print(f"You've selected Supa big boys pizza, costs ₦{big_boys_price}")
            print(f"\nTotal cost of {boxes} boxes of pizza is ₦{total}")
            print("===================")
            print(f"Your bill is ₦{total}")
            print("===================")
            print(f"Total slices of pizzas in {boxes} boxes are {total_slices}")
            print(f"\nThere will be {left_over} left over pizzas after all guest have been served a pizza each")
        case "4":
            cost = odugwu_price * boxes
            total_slices = odugwu_slices * boxes
            total = odugwu_price * boxes
            left_over = total_slices - guest
            print(f"You've selected Odogwu pizza, costs ₦{odugwu_price}")
            print(f"\nTotal cost of {boxes} boxes of pizza is ₦{total}")
            print("===================")
            print(f"Your bill is ₦{total}")
            print("===================")
            print(f"Total slices of pizzas in {boxes} boxes are {total_slices}")
            print(f"\nThere will be {left_over} left over pizzas after all guest have been served a pizza each")

        case "5": 
            print("Thank you for shopping with us")
            exit()
                

        case _:
                print("Invalid pizza selection!")
                exit()


pizza_type(selected_pizza_type)









 
