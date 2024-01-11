# get the names
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = name1.lower() + name2.lower()

# god this is stupid

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")

true = t + r + u + e
love = l + o + v + e

# adding some stuff to make this suck less
# like accounting for cases where the "love" score is greater than 10

if love > 10:
    love = love - 10
    true = true + 1
elif love > 20:
    love = love - 20
    true = true + 2
else:
    true = 10
    love = 0

# back to the normal code
love_score = int(str(true) + str(love))

# seriously, I get the purpose of the exercise, but this is stupid
# do kids actually believe this shit?

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like Coke and Mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.") 
else:
    print(f"Your score is {love_score}.")

