def leapYear():
    if Year % 4 == 0:
        if Year % 100 == 0:
            if Year % 400 == 0:
                print("leap Year")
                return True
            else:
                print("Not a leap Year")
                return False
        else:
            print("leap Year")
            return True
    else:
        print("Not a leap Year")
        return False

def days_of_month(Year,month):
    """take's Year and month to specify the no of days"""
    if month>12 or month<1:
        return "In_correct input"
    month_days = [31,28,31,30,31,30,31,31,30,31,30]
    if leapYear(Year) and month == 2:
        return 29
    return month_days[month-1]

Year = int(input("Enter Year: "))
month = int(input("Enter a month: "))
days = days_of_month(Year,month)
print(days)