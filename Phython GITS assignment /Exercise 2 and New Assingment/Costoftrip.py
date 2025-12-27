#ask a user to enter the distance to drive
#ask user to enter the fuel efficiency of the car in miles per gallon
#ask user to enter price per gallon

#display the cost of trip (print)

distance = float(input("Enter the distance to drive: ")) 

miles_per_gallon = float(input("Enter the fuel of car in miles per gallon: ")) 

gallon_price = float(input("Enter the price per gallon: ")) 


if distance > 0 and miles_per_gallon > 0 and gallon_price  > 0:
        cost_of_trip = distance * gallon_price / miles_per_gallon
        print(f"Cost of trip is = " , cost_of_trip)






