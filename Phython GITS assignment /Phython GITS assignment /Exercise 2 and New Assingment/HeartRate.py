#PSUEDOCODE
#collect the age of a user, calculate the maximum heart range (220) of the user per minute
#when you minus the maximum heart range by the user age, 220 - age,
#the display the output and then calculate the target heart rate, 
#which is the combination of the lower rateof 0.50% and higher rate 0.85% of 
#target trainig range by multiply by the maximum heart range, then
#display the output of the range. 

age = int(input("Enter your age: "))

max_heart_rate_min = 220 - age

print("maximum rate: ", max_heart_rate_min)


lower_rate = max_heart_rate_min * 0.50

higher_rate = max_heart_rate_min * 0.85



print("target heart range: " , lower_rate, "to", higher_rate)


