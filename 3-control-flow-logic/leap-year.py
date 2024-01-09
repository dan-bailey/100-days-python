# check leap year
year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leapStatus = "leap"
        else:
            leapStatus = "not leap"
    else:
        leapStatus = "leap"
else:
    leapStatus = "not leap"

print(f"The year {year} is {leapStatus}.")