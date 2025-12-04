#ask a user for amount the user paid
#ask same user if his a member of the club ("yes" or "no")
#now lets apply discount
#if the total bill paid is above or equal to a thousand dollars and the user is a member, he gets a discount price of 10%off which is 0.10%
#if the total bill paid by the user is equals to a thousand of higher than a thousand and the user is not a member he gets five percent discount which is 0.05%
#else, he gets no discount, display the total amount paid and a message saying No Discount


amount = int(input("How much are you paying: "))
member = input("Are you a member? Yes or No:  ").lower()

if amount >= 1000 and member == "yes":
    print("10% off")
    print("You are qualified for the DISCOUNT and your payment is 900")


elif amount >= 1000 and member == "no":
    print("5% off")
    print("You are qualified for the DISCOUNT and your payment is 950")

else:

    print("You are not qualified for a DISCOUNT at this time")
    print("total amount paid by you = ", amount)
