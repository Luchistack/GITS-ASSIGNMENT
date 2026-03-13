base_pay = 5000

def collection_pay(collection_rate):

    if collection_rate >= 70:
        
        amount_per_parcel = 500
             
    elif collection_rate >= 60 and collection_rate <= 69:

        amount_per_parcel = 250

    elif collection_rate >= 50 and collection_rate <= 59:

        amount_per_parcel = 200
    
    else:
        amount_per_parcel = 160

    return base_pay + (collection_rate * amount_per_parcel) 

