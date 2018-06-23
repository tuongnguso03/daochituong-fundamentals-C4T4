mass = int(input("Enter your weight (kg): "))
height = int(input ("Enter your height (cm): "))/100
BMI = mass/height**2
print("Your BMI : ",BMI)
if BMI < 16:
    print("Severely underweight")
elif BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("Overweight")   
else:
    print("Obese") 

