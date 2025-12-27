
def check_code(price, code):  
        discount_one = price - 10
        discount_two = price / 2

        if code == "SAVE10":     
            return discount_one
                   
        elif code == "HALFOFF":    
            return discount_two
        
        else:
            return price

