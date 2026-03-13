age = int(input("Enter your age: "))

if age >= 65:
    print("Your ticket price is $8")
elif age >= 13:
    print("Your ticket price is $12")
elif age >= 5:
    print("Your ticket price is $5")
else:
    print("Your ticket is free")
