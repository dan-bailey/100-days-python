sum = 0
countTo = int(input("Enter a number: "))
for i in range(1, countTo + 1):
    if i % 2 == 0:
        sum += i
print(sum)
