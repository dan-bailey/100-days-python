import random

# list comprehension
numbers = [1, 2, 3, 4, 5]
new_list = [n*n for n in numbers]
print(new_list)

# conditional list comprehension
new_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
newer_list = [n for n in new_numbers if n % 2 == 0]
print(newer_list)

# more of the conditional list comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Edwin", "Freddie"]
name_list = [name.upper() for name in names if len(name) >= 5]
print(name_list)

# common items using list comprehension
f1 = [1, 2, 3]
f2 = [2, 3, 4, 0, 9]
result = [n for n in f1 if n in f2]

print(result)

# dictionary comprehension
newnames = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Edwin", "Freddie"]
student_scores = { item:random.randint(1, 100) for item in newnames }
print(student_scores)

passed_students = { student:score for (student, score) in student_scores.items() if score >= 71 }
print(passed_students)