Year = int(input("Enter Year: "))

if Year % 4 == 0:
    if Year % 100 == 0:
        if Year % 400 == 0:
            print("leap Year")
        else:
            print("Not a leap Year")
    else:
        print("leap Year")
else:
    print("Not a leap Year")