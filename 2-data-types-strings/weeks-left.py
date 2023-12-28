age = input("How old are you? ")
lifetime = input("How long do you expect to live? ")
totalWeeks = int(lifetime) * 52
currentWeeks = int(age) * 52
weeksLeft = totalWeeks - currentWeeks
print(f"You have {weeksLeft} weeks left to live.")