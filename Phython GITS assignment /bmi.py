weight = float(input("Enter weight"))

height = float(input("Enter height"))

bmi = weight/(height*height)
compute_bmi = bmi

if compute_bmi < 18.5:
    print("Underweight")

elif 18.5 <= compute_bmi < 24.9:
    print("Normal")

elif 25 <= compute_bmi  < 29.9:
    print("Overweight")

else:

    print("Obese")

