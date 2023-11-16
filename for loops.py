students_heights = [180,124,165,173,189,169,147]
count = 0
total = 0
for item in students_heights:
    count +=1
    total +=item
print(total/count)#sun(),len()

student_scores = [78,65,89,86,55,91,64,89]
larges = 0;
for items in student_scores:
    if items>larges:
        larges=items
print(larges)#max()

total_no = 0
for items in range(1,101):
    total_no += items
print(total_no)

total_even = 0
for items in range(1,101):#range(1,101,2) generates even no's
    if items%2==0:
        total_even+=items
print(total_even)


