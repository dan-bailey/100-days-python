import random
# life is so much easier when you start using libraries
import string_utils

charCount = int(input("How many characters do you want in your password? "))
symbolCount = int(input("How many symbols do you want in your password? ")) 
numberCount = int(input("How many numbers do you want in your password? ")) 

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
           'p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F',
           'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W',
           'X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','[',']',
           '|','\\',';',':','"',"'",'<','>',',','.','/','?']

# Easy Level would be letters, numbers, then symbols
# Hard Level would be random order, but that's not complicated, either

# Build the base string
password = ""
for i in range(1, charCount + 1):
    password += random.choice(letters)
for i in range(1, symbolCount + 1):
    password += random.choice(symbols)
# note that the numbers list is stored as strings, no conversion necessary
for i in range(1, numberCount + 1):
    password += random.choice(numbers)

scramble = string_utils.shuffle(password)

print(f"Your password base is: {password}")
print(f"Your password is: {scramble}")