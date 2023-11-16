import random
import string

letters = int(input("Enter the no of letters in your password:"))
symbols = int(input("Enter the no of symbols in your password:"))
numbers = int(input("Enter the no of numbers in your password:"))
password_array=''
for items in range(letters):
    password_array += random.choice(string.ascii_letters)
for items in range(symbols):
    password_array += random.choice(string.digits)
for items in range(numbers):
    password_array += random.choice(string.punctuation)
print(f"Weak = {password_array}")
password = ''.join(random.sample(password_array,len(password_array)))
print(f"Strong = {password}")