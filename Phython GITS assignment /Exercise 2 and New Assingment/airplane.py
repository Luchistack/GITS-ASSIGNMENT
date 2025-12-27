#in defining the run way length of a airplane
#a= accelaration
#v = speed
#lenght = v**2 which is speed **2 divided by two times the value of accelartion, which is 2a

acceleration = float(input("Enter acceleration: "))
speed = float(input("Enter Runway Speed: "))

length = (speed**2)/(2*acceleration)


print("The minimun runaway length for the airplane; ", round(length, 2))



