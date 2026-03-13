
balance = 0
withdraw_balance = 0

print("Welcome to transaction Log App")

def menu ():
        print("\n1. Deposit\n2. Withdraw\n3. Show Transactions\n4. Exit");

def deposit():
        deposit_amount = int(input("Enter deposit amount: "))
        balance += deposit_amount
        print(f"Deposited:₦{deposit_amount} | New Balance: ₦{balance} " )
        print(f"\n=======================================" )


def withdraw():
        withdraw = int(input("Enter withdrawal amount:₦ "))
        if withdrawt <= withdraw_balance:
            withdraw_balance -= withdraw
            print(f"Withdrew:₦{withdraw} | New Balance: ₦{withdraw_balance} " )
            print(f"\n=======================================" )
        else:
            print("Insufficient balance")

def transactions():
        print("Transaction so far: ")
        if not transactions:
               print("no transactoin yet")
        else:  
            for t in transactions:
                print(f"1. Deposited:₦{deposit} | New Balance: ₦{new_balance} " )
                print(f"2. Withdrew:₦{withdraw} | New Balance: ₦{withdraw_balance} " )
                print(f"\n=======================================" )


while True:
     menu() 
     choice = int(input("\nEnter your choice: "))
     if choice == 1:
            deposit()
     if choice == 2:
            withdraw()
     if choice == 3:
            transactions()
     if choice == 1:
            deposit()
            final_balance = withdraw_balance
            print(f"FInal Balance:₦ {withdraw_balance}")

            break;
