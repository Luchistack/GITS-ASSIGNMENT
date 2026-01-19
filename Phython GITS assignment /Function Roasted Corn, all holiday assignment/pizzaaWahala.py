
#this program acts like a pizza shop assistant.
#It shows the menu, collects customer choices, calculates slices, checks leftovers, and prints the final bill in naira


supa_price = 2000
small_price = 3000
big_boys_price = 3600
odugwu_price = 4200 

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

        1. Supa size pizza @ ₦2000
        2. Small Money pizza @ ₦3000
        3. Big Boys pizza @ ₦3600
        4. Odugwu pizza @ ₦4200
        5. Quit

        Select from the available options or enter 5 to quit
        """)




while True:
    menu()

    selected_pizza_type = input("what type of pizza do you want to buy: ").lower()

def details(selected_pizza_type):
    match selected_pizza_type:
        case "supa size":
            print("======================================")
            print(f"you just selected {selected_pizza_type} @ Supa size pizza")
            print(f"Supa size pizza costs ₦{supa_price}")
            print("============================")

        case "small money":
            print("=======================================")
            print(f"you just selected {selected_pizza_type} @ Small Money pizza")
            print(f"Small money pizza costs ₦{small_price}")
            print("============================")


        case "big boys":
            print("=======================================")
            print(f"you just selected {selected_pizza_type} @ Big Boys pizza")
            print(f"Big boys pizza costs ₦{big_boys_price}")
            print("=============================")

        case "odugwu pizza":
            print("=======================================")
            print(f"you just selected {selected_pizza_type} @ Odugwu pizza")
            print(f"Odogwu pizza costs ₦{odugwu_price}")
            print("=============================")


        case "quit": 
            print("Thank you for shopping with us")
        break

        case _:
            print("Invalid pizza selection!")
              


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
        case "supa size":
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
     

        case "small money":
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

        case "big boys":
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
        case "odugwu":
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

        case "Quit": 
            print("Thank you for shopping with us")
            exit()
                

        case _:
                print("Invalid pizza selection!")
                exit()


pizza_type(selected_pizza_type)









 
