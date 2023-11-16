for items in range(1,101):
    if items % 3 == 0 and items % 5 == 0:
        print("Fizz Buzz")
    elif items % 3 == 0:
        print("fizz")
    elif items % 5 == 0:
        print("Buzz")
    else:
        print(items)