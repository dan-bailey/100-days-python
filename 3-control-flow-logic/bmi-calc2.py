# get height in meters
height = float(input("Enter your height in meters: "))
# get weight in kilos
weight = int(input("Enter your weight in kilograms: "))
# calculate BMI
bmi = weight / (height * height)

# set weight conditionals
if bmi < 18.5:
    bmiStatus = "underweight"
elif bmi >= 18.5 and bmi < 25:
    bmiStatus = "normal"
elif bmi >= 25 and bmi < 30:
    bmiStatus = "overweight"
elif bmi >= 30 and bmi < 35:
    bmiStatus = "obese"
else:
    bmiStatus = "clinically obese"

# print results
print(f"Your BMI is {bmi} and you are {bmiStatus}.")
