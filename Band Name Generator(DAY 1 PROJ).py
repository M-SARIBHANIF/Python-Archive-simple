import random
print("Welcome to the Band Name Generator")
Comp_1 = input("Enter name of Comp one: \n")
Comp_2 = input("Enter name of Comp Tow: \n")

Choice = random.randint(0,1)
if Choice == 0:
    print("Your Band Name: ",Comp_1+Comp_2)
else:
    print("Your Band Name: ",Comp_2+Comp_1)
