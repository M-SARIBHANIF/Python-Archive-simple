import pandas
students_dict = {
    "students":["Angela", "James", "Lily"],
    "Scores":[56, 76, 98]
}
for (key,value) in students_dict.items():
    print(key,value)
students_data_frame= pandas.DataFrame(students_dict)
print(students_data_frame)

for (key,value) in students_data_frame.items():
    print(key,value)
for(index,row) in students_data_frame.iterrows():
    print(index,row.students,row.Scores)