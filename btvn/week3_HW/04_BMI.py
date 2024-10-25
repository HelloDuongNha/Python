height = float(input("What is your height in meters? "))
weight = float(input("What is your weight in kilograms? "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    category = "Underweight"
elif bmi < 24.9:
    category = "Normal weight"
elif bmi < 29.9:
    category = "Overweight"
else:
    category = "Obese"
print("Your BMI is", bmi, "and you are", category, ".")