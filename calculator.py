def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def Multiply(n1,n2):
    return n1*n2
def Divide(n1,n2):
    return n1/n2
def calculation():
    """ takes inputs chooses key from dictionary of choice and converts into function call"""
    Choice = {
        "+":add,"-":subtract,"*":Multiply,"/":Divide
    }
    number_1 = float(input("Enter a no: "))
    for items in Choice:
        print(items)
    Continue = True
    while Continue == True:
        operation_symbol =input("Pick a symbol form the lines above: ")
        number_2 = float(input("Enter a no:  "))
        calculation = Choice[operation_symbol]
        Answer = calculation(number_1,number_2)

        print(f"{number_1}{operation_symbol}{number_2} = {Answer}")
        if input("type 'y' for more operations and new for 'new' calculation") == 'y':
            number_1 = Answer
        elif input("type 'new' for new calculation") == 'new' :
            calculation()
        else:
            Continue = False
calculation()