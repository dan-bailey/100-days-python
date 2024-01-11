import random

names = ["Dan", "Didi", "Gertie", "Joey", "Lucky", "Schultzie", "Cole", "Eddy", "Sam"]
num_names = len(names)
random_index = random.randint(0, num_names - 1)
print(names[random_index] + " is going to buy the meal today!")
