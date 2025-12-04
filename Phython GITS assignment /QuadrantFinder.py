
#1. collect two intergers, x and y
#2. 
#3. print out Q1, if x is greater than zero and y is also greater than zero
#4. print out Q2 if x is lesser than zero and y is greater than zero
#5. print out Q3, if x is lesser than zero and y is also lesser than zero
#6. print out Q4, if x is greater than zero and y is lesser than zero
#7. print out Origin, if both is zero
#8. pnt out X-axis if y is equal to zero and x is not equal to zero
#9. print out Y-axis if x is equal to zero ans y is not equal to zero

x = int(input("Enter  a number: "))

y = int(input("Enter  a number: "))

if ( x > 0  and y > 0):
    print("Q1")

elif ( x < 0 and  y > 0):
    print("Q2")

elif (x < 0 and y < 0):
    print("Q3")

elif (x > 0 and y < 0):
    print("Q4")

elif (x == 0 and y == 0):
    print("Origin")

elif (y == 0 and x != 0):
    print("X-axis")

elif (x== 0 and y != 0):
    print("Y-axis")



