import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanore", "Freddie"]
random_score = {student:random.randint(1,100) for student in names}
print(random_score)
passed_students = { students:score for (students,score) in random_score.items() if score >= 60}
print(passed_students)