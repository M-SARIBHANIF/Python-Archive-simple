height=float(input("Enter your height(meters): "))
weight=int(input("Enter your weight(kilo-gram): "))

BMI = weight/(height**2)
print(round(BMI))
#or
print(int(BMI))