import math
def Greet(name,location):
    print("Hello")
    print("WellCome",name)
    print(f"your location is ->{location}")


Greet(name=input("Enter your name: "),location=input("Enter your location: "))

def Area_Calculator(height,width,coverage):
    area = height * width
    no_fo_cans = math.ceil(area/coverage)
    print(f"the no of cans you need to buy is: {round(no_fo_cans)}")

Area_Calculator(height=int(input("Enter height of wall: ")),width=int(input("Enter width of wall: ")),coverage=int(input("Enter coverage of wall: ")))


def chk_Prime_no(n):
    for numbers in range (2,n):
        if n%numbers !=0: 
            print("prime no")
        else:
            print("prime no")

chk_Prime_no(n=int((input("enter a no"))))