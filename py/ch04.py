#BMI Program

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: ")) 
bmi = weight / (height ** 2) /100
print("Your BMI is: ", bmi)

#BMI Categories

if bmi < 18.5:
    print("You are underweight.")
elif bmi >= 18.5 and bmi < 25:
    print("You are normal weight.")
elif bmi >= 25 and bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")