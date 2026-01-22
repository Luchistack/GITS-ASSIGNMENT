
base_pay = 5000
 
def collection_table():
    print("""              
                    BACK TO SENDER LOGISTICS SERVICES COMMISSION TABLE
               ------------------------------------------------------------              
              | Collection Rate |    Amount per Parcel     |   Base Pay   |
              -------------------------------------------------------------                      
  
              |Less than 50%    |         ₦160             |    ₦5,000 
             
              |50% - 59%        |         ₦200             |    ₦5,000  

              |60% - 69%        |         ₦250             |    ₦5,000  
             
              |>=70%            |         ₦500             |    ₦5,000 
              -------------------------------------------------------------
        """)

collection_table()



riders_name = input("\nEnter Riders Name: ").strip()
print(f"\nDear {riders_name}, Lets check the tasks you made today")

#if riders_name = " ":
#    print("invalid name, enter a name")
#    exit()

collection_rate = int(input("\nEnter Number Of Succcessfull Delivery Done Today: "))

if collection_rate < 0 or collection_rate > 100:
    print("\nInvalid Entry! Collection rate must be between 0 and 100.")
    exit()


def collection_pay(collection_rate):

    if collection_rate >= 70:
        
        amount_per_parcel = 500
             
    elif collection_rate >= 60 and collection_rate <= 69:

        amount_per_parcel = 250

    elif collection_rate >= 50 and collection_rate <= 59:

        amount_per_parcel = 200
    
    else:
        amount_per_parcel = 160

    expected_returns = base_pay + (collection_rate * amount_per_parcel) 
    return expected_returns

expected_returns = collection_pay(collection_rate)

print(f"""\n Dear {riders_name},
 Successful Deliveries: {collection_rate} 
 Total Earnings: ₦{expected_returns} 
""")

