print("Welcome to tip Calculator")
Initial_Bill = float(input("What was the total bill?: $"))
Tip=int(input("What percentage tip would like to give? 10%,12% or 15%?: "))
Total_persons=int(input("How many total People to split the bill: "))

if Tip == 10:
    final = (Initial_Bill+10/100)/Total_persons
    print(f"Each person has to pay ${round(final,2)}")
elif Tip == 12:
    final = (Initial_Bill+12/100)/Total_persons
    print(f"Each person has to pay ${round(final,2)}")
else:
    final = (Initial_Bill+15/100)/Total_persons
    print(f"Each person has to pay ${round(final,2)}")

#In case if strict formating
formatted="{:.2f}".format(final)
print(final)
