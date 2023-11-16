Size = input("What Size Pizza Do You Want\nSmall(S)\nMedium(M)\nLarge(L)\n")
Pepperoni = input("Do you Want Extra pepperonie(Y or N): ")
Cheese = input("Do You Want Extra Cheese(Y or N): ")
Cost = 0
if Size == "S":
    Cost +=15
    if Pepperoni == "Y":
        Cost +=2
elif Size == "M":
    Cost +=20
    if Pepperoni == "Y":
        Cost +=3
elif Size == "L":
    Cost +=25
    if Pepperoni == "Y":
        Cost +=3
if Cheese == "Y":
    Cost +=1
print(f"Your total Cost is-->${Cost}")

