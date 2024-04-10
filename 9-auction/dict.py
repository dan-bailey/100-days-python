# dictionary = key/value pairs
# {key: value}
# looks like JSON
# key must be unique
# key must be immutable (string, number, tuple)

programming_dictionary = {
    "Bug": "You fucked up.",
    "Function": "The thing you fucked up."
}

# print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "Your fuckup, revisited."
# print(programming_dictionary)
# print("")
# print("")
# print("")
programming_dictionary["Loop"] = {"Loop": "See also: loop."}
programming_dictionary["Shit"] = [2, 3, 4, 5, 6]
# print(programming_dictionary["Loop"]["Loop"])
# print (str(programming_dictionary["Shit"][2]))

#loop thru
for thing in programming_dictionary:
    print(thing)