

balance = 0
deposit = 0
withdraw = 0

print("Welcome to transaction Log App")

def menu ():
        print("\n1. Deposit\n2. Withdraw\n3. Show Transactions History\n4. Exit the App");


while True:
        menu()
        choice = int(input("\nEnter your choice: "))
    

        match choice:
            case 1:
                while True:
                    deposit = float(input("Enter deposit amount: "))
                    balance += deposit
                    print(f"You've successfully Deposited:₦{deposit}  👌️")
                    
                    print("=" * 35)

                    new_deposit_transaction = input("\nWould you like to perform another deposit transaction YES/NO? ").casefold()
       

                    if new_deposit_transaction != "yes" and new_deposit_transaction != "no":
                       print("invalid entry\n Thank You For Using This App! 🤨️ ")
                       break

                    if new_deposit_transaction == "no":
                       break


            case 2: 
                while True:        
                    withdraw = float(input("Enter withdrawal amount:₦ "))
                    if withdraw > balance:
                        print("Insufficient funds, SAPA has dealt with you 🫢️")
                        
            
                    else:
                        balance -= withdraw 
                        print(f"You've successfuly withdrew ₦{withdraw} 🤑️")
                        print(f"Withdrew:₦{withdraw} | New Balance: ₦{balance} " )
                        print("=" * 35)

                        new_withdraw_transaction = input("\nWould you like to perform another withdraw transaction YES/NO? ").casefold()

                        
                        if new_withdraw_transaction != "yes" and new_withdraw_transaction != "no":
                           print("invalid entry\n Thank You For Using This App!")
                           break
                        
        
                        if new_withdraw_transaction == "no":
                           break


            case 3:
                while True:
                    print("Transaction history: ")
                    print(f"Recent Amount Deposited:₦{deposit} | Recent Amount Withdrew:₦{withdraw}  " )
                    print(f"Current Balance: ₦{balance} " )
                    print("=" * 35)

                    new_transaction = input("\nWould you like to check your Transaction history again YES/NO? 🤔️").casefold()


                    if new_transaction != "yes" and new_transaction != "no":
                       print("invalid entry\n Thank You For Using This App!")
                       break

                    if new_transaction == "no":
                       break

            case 4:
                        current_balance = balance
                        print(f"Your Current Balance:₦ {current_balance}")
                        print("Thank you for banking with us 🏦️")
                        break




                   

    

     

