#List Comprehension
numbers = [1, 2, 3]
new_no = [n*2 for n in numbers]
print(new_no)

name = "Ostrava"
new_list = [letters for letters in name]
print(new_list)

list = range(0,6)
new_range = [n*2 for n in list]
print(new_range)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
upper_case = [n.upper() for n in names if len(n)>4]
print(upper_case)

numbers = [1,2,3,4,5,6,7,8]
squared=[n**2 for n in numbers]
print(squared)

numbers_total = [1,2,3,4,5,6,7,8]
even = [n for n in numbers_total if n%2 == 0]
print(even)