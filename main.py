import string
import re
import random


def pass_gen(length, security):

    bad_chars = ['`', "'", '"']
    special_chars = [char for char in string.punctuation if char not in bad_chars]
    lower_letters = [letter for letter in string.ascii_lowercase]
    upper_letters = [letter for letter in string.ascii_uppercase]
    numbers = [str(num) for num in range(10)]

    password = ""

    chars = [special_chars, lower_letters, upper_letters, numbers]

    if security == "max":
        for _ in range(length):
            if len(password) == 0:
                password += random.choice(special_chars)
                password += random.choice(upper_letters)
                password += random.choice(lower_letters)
                password += random.choice(numbers)
            else:

                rand_selection = random.choice(chars)
                rand_chars = rand_selection[random.randrange(len(rand_selection))]
                
                password += rand_chars

            if len(password) >= length:
                break
    return(password)

print(pass_gen(12, "max"))