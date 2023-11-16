#add n numbers
def add(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    print(f"{sum} = {numbers[0]}+{numbers[1]}+{numbers[2]}+{numbers[3]}+{numbers[4]}"
          f"+{numbers[5]}+{numbers[6]}+{numbers[7]}+{numbers[9]}")

add(1,2,3,4,5,6,7,8,9,10)

def calculate(n,**kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

class Sun:
    def __init__(self,**kw):
        self.Heat = kw.get("Heat")
        self.Praise =  kw.get("Praise")

my_sun = Sun(Heat="Yes",Praise="Indeed")
print(my_sun.Heat,my_sun.Praise)