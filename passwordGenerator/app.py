import random
import string

password_length = ""
generated_password = ""
is_of_correct_type = False

while not is_of_correct_type:
    try:
        password_length = int(input("How many characters should the password contain? (Between 8 and 20 characters)\n"))
        if not 8 <= password_length <= 20:
            print("\nInput a number between 8 and 20")
            is_of_correct_type = False
        else:
            is_of_correct_type = True
    except ValueError:
        print("\nWrite a number please")

for number in range(password_length):
    random_letter = random.choice(string.ascii_letters)
    random_number = random.choice(string.digits)
    random_symbol = random.choice(string.punctuation)
    random_value = random.choice([random_number, random_letter, random_symbol])
    generated_password = generated_password + random_value
else:
    print("Your password is: " + generated_password)

