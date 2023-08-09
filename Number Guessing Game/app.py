import random

random_num = random.randint(0, 10)
used_clues = 0
guessed_num = ""

print("Can you guess the number correctly between 0 and 10?.")

while used_clues < 5 and guessed_num != random_num:
    used_clues += 1
    try:
        guessed_num = int(input("Enter a number: "))
        if guessed_num == random_num:
            print("Congrats! The number was " + str(random_num) + ". You got it in " + str(used_clues) + " tries.")
        elif guessed_num != random_num and used_clues == 5:
            print("You've used all your tries.")
        else:
            print("Wrong number. You have " + str(5 - used_clues) + " tries left. Try again.")
    except ValueError as err:
        print("Not a number")
