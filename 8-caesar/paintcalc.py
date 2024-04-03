import math

def paintcalc(width, height, coverage):
    cans = (width * height) / coverage
    return math.ceil(cans)

# Run it
test_w = int(input("Width of wall: "))
test_h = int(input("Height of wall: "))
test_c = 5

print(f"You will need {paintcalc(test_w, test_h, test_c)} cans of paint.")