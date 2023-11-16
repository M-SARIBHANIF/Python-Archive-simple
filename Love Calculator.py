Name_Yours = input("Enter Your Name: ").lower()
Name_Other = input("Enter Your Other's Name: ").lower()
Final_Name = Name_Yours + Name_Other
T_Count_1 = 0
T_Count_2 = 0
T_Count_1 += Final_Name.count("t")
T_Count_1 += Final_Name.count("r")
T_Count_1 += Final_Name.count("u")
T_Count_1 += Final_Name.count("e")

T_Count_2 += Final_Name.count("l")
T_Count_2 += Final_Name.count("o")
T_Count_2 += Final_Name.count("v")
T_Count_2 += Final_Name.count("e")

final_Score = str(T_Count_1)+str(T_Count_2)
if int(final_Score) < 10 or int(final_Score) > 90:
    print(f"Your Score is {final_Score}, you go together like coke and mentos")
elif int(final_Score) >= 40 and int(final_Score) <= 50:
    print(f"Your Score is {final_Score},you are alright together.")
else:
    print(f"Your score is {final_Score}")





