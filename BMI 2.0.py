height=float(input("Enter your height(meters): "))
weight=int(input("Enter your weight(kilo-gram): "))

BMI = weight/(height**2)
Wht = round(BMI)
if Wht < 18.5:
    print("Underweight")
elif Wht > 18.5 and Wht < 25:
        print("Normal Weight")
elif Wht > 25 and Wht < 30:
        print("Overweight")
elif Wht > 30 and Wht < 35:
        print("Obese")
elif Wht > 35:
        print("Clinically Obese")

print(round(BMI))