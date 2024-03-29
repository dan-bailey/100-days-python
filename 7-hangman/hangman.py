import os
import random

def get_word():
    # randomly select a word from a list
    word_list = ["python", "java", "kotlin", "javascript"]
    return (random.choice(word_list)).upper()

def get_guess():
    # get a letter from the user and return it
    # probably could use some error trapping in here to ensure it's a letter
    # and that it hasn't been guessed before, but this is a simple exercise in
    # string manipulation and basic loops
    return (input("Guess a letter: ")).upper()

def print_gallows():
    print("  +---+")
    print("  |   |")
    print("      |")
    print("      |")
    print("      |")
    print("      |")
    print("=========")

def print_head():
    print("  +---+")
    print("  |   |")
    print("  O   |")
    print("      |")
    print("      |")
    print("      |")
    print("=========")

def print_body():
    print("  +---+")
    print("  |   |")
    print("  O   |")
    print("  |   |")
    print("      |")
    print("      |")
    print("=========")

def print_left_arm():
    print("  +---+")
    print("  |   |")
    print("  O   |")
    print(" /|   |")
    print("      |")
    print("      |")
    print("=========")

def print_right_arm( ):
    print("  +---+")
    print("  |   |")
    print("  O   |")
    print(" /|\  |")
    print("      |")
    print("      |")
    print("=========")

def print_left_leg():
    print("  +---+")
    print("  |   |")
    print("  O   |")
    print(" /|\  |")
    print(" /    |")
    print("      |")
    print("=========")

def print_right_leg():
    print("  +---+")
    print("  |   |")
    print("  O   |")
    print(" /|\  |")
    print(" / \  |")
    print("      |")
    print("=========")
    print("GAME OVER")

def display_header(misses):
    os.system("clear")
    print("The word length is: " + word_length)
    print("Letters guessed: " + guesses_list)
    print("")
    print("Your word so far: " + display_word)
    print("")
    if misses == 0:
        print_gallows()
    elif misses == 1:
        print_head()
    elif misses == 2:
        print_body()
    elif misses == 3:
        print_left_arm()
    elif misses == 4:
        print_right_arm()
    elif misses == 5:
        print_left_leg()
    elif misses == 6:
        print_right_leg()

def generate_blanks(count):
    temp = ""
    for x in range(int(count)):
        temp = temp + "_"
    return temp



## clear the screen
os.system("clear")

## start game
missed_guesses = 0
end_condition = ""
target_word = get_word()
guesses_list = "" # this starts as blanks, but will be filled in as the user incorrectly guesses letters
word_length = str(len(target_word))
display_word = generate_blanks(word_length) # this starts as blanks, but will be filled in as the user correctly guesses letters

while end_condition != "gameover":
    ## Step one: display the header, get the guess, and add it to the list
    display_header(missed_guesses)
    print("")
    guess = get_guess()

    ## Step two: check the guess against the word
    current_state = display_word
    guesses_list = guesses_list + guess + " "
    count = 0
    for letter in target_word:
        if letter == guess:
            # convert to a list
            display_list = list(display_word)
            # replace the letter in the list
            display_list[count] = guess
            # convert back to a string
            display_word = "".join(display_list)
        count += 1
    if current_state == display_word:
        missed_guesses = missed_guesses + 1

    ## Step three: check to see if at max guesses or if the word is complete
    if missed_guesses == 6:
        final_message = "GAME OVER - OW MY NECK"
        end_condition = "gameover"

    if display_word == target_word:
        final_message = "GAME OVER - YOU WIN"
        end_condition = "gameover"

display_header(missed_guesses)
print("")
print (final_message)
