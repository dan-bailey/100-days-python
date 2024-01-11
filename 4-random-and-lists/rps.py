import random

human_choice =  int(input("Rock (0), Paper(1), or Scissors(2)? "))
# realistically, this would have some sort of input scrubbing
# but this is just another annoying exercise

item = ["Rock", "Paper", "Scissors"]
num_items = len(item)
computer_choice = random.randint(0, num_items - 1)

print(f"You chose {item[human_choice]}.")
print(f"The computer chose {item[computer_choice]}.")
if human_choice == computer_choice:
    print("You tied!")
elif human_choice == 0 and computer_choice == 1:
    print("You lose!")
elif human_choice == 0 and computer_choice == 2:
    print("You win!")
elif human_choice == 1 and computer_choice == 0:
    print("You win!")
elif human_choice == 1 and computer_choice == 2:
    print("You lose!")
elif human_choice == 2 and computer_choice == 0:
    print("You lose!")
elif human_choice == 2 and computer_choice == 1:
    print("You win!")
else:
    print("Wait, something went wrong.")
