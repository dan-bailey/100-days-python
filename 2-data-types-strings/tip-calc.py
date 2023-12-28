bill = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

percentage_as_float = float(percentage) / 100
totalBill = float(bill) * (1 + percentage_as_float)
billPerPerson = round((totalBill / int(people)), 2)
billPerPerson = "{:.2f}".format(billPerPerson)

print(f"Each person should pay: ${billPerPerson}")
