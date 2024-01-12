scores = [10, 90, 20, 43, 77, 55, 25, 13]
highest = 0
for s in scores:
    if s > highest:
        highest = s
print(f"The highest score in the class is: {highest}")
print(f"This could've been done more easily. Using the max function, the highest score is: {max(scores)}")

# I understand that this was yet another tedious exercise in lists