import os

bids = []
highest_bid = 0
answer = "yes"
while answer == "yes":
    os.system('clear')
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids.append({"name": name, "bid": bid})
    answer = input("Are there any other bidders? Type 'yes' or 'no'. \n")

for bid in bids:
    if bid["bid"] > highest_bid:
        highest_bid = bid["bid"]
        winner = bid["name"]
print(f"The winner is {winner} with a bid of ${highest_bid}")