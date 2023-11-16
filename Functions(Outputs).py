def Formate_name(F_name,L_name):
    if F_name == "" or L_name =="":
        return "In-Correct String"
    Full_name = F_name.title()+L_name.title()
    return Full_name

print(Formate_name(input("Enter first name"),input("Enter Last name")))