#ask user to input temperature
# along with celcuis measurement or fahrenheit
# input celsuis if fahrenheit is not provided by user
# user  should input threshold value for triggering a heat advisory
#use the function to convert to the opposite unit using c formula to convert from F to C or f formula to convert from C to F
#check if converted temperature is below or above given threshold
#if its below, return "cold advisory"
# if its equal or above to threshod return "Heat alert"
#
#accure accuracy of temperature conversion and advisory mesaage logic by writing and running validation tests using TDD

#def measurement (temperature, celcius, fahrenheit, threshold)
#                                print(f"measurement {temperature} {celcius} {fahrenheit} {threshold}")
#                                print("celcuis measurement {celcius}")
#                                print("fahrenheit measurement {fahrenheit}")
#                                print("threshold value {threshold}")
#measurement

fahrenheit = " "
celsuis = " "
measurement = 0

celsuis = (measurement - 32) * 5/9 #fahrenheit_to_celsuis
fahrenheit = ((measurement * 9/5) + 32) #celsius_to_fahrenheit

temperature = float(input("Enter temperature value: "))
measurement = float(input("Enter Celsius or Fahrenheit: "))
heat_threshold = float(input("Enter heat threshold: "))

if measurement == 55:
    print(f"Measurement is %f" , fahrenheit)
    print("Fahrenheit coverted to celcuis is ", celsuis)   
 
elif measurement == 40:
    print(f"Measurement is ", fahrenheit)
    print("Celsuis coverted to fahrenheit is ", fahrenheit)   
 
