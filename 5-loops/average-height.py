student_heights = [180, 124, 165, 173, 189, 169, 146]
total_height = 0
for h in student_heights:
    total_height += h
number_of_students = len(student_heights)
average_height = round(total_height / number_of_students)
print(average_height)