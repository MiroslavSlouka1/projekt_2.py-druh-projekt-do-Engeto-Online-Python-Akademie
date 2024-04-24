"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Miroslav Slouka
email: miroslav.slouka@kitron.com
discord: mirek_63517

"""

import time
from random import choice


def line_dashes():
    print("-" * 47)


def welcome():
    print("Hi there!")
    line_dashes()
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    line_dashes()
    print("Enter a number:")


def statistics(count, start_time):
    print("Correct, you've guessed the right number")
    print(f"in {count} guesses!")
    line_dashes()
    rating = ("amazing", "average", "not so good", "you're out of shape")
    index = 0  # count 1-5

    if 5 < count < 10:
        index = 1

    if 9 < count < 15:
        index = 2

    if 14 < count:
        index = 3

    print(f"That's {rating[index]}")

    aktual_unix_timestamp = time.time()
    duration = (int(aktual_unix_timestamp - start_time))
    time_structure = time.gmtime(duration)
    time_string = time.strftime("%H:%M:%S", time_structure)
    print("Duration in hours, minutes, and seconds is:", time_string)
    exit()


def guessed_number():
    gen_numbers = ""
    list_numbers = list(range(1, 10))
    for i in range(4):
        if i == 1:
            list_numbers.append(0)
        random_number = choice(list_numbers)
        list_numbers.remove(random_number)
        gen_numbers += str(random_number)
    return gen_numbers


def input_number():
    correct = True
    line_dashes()
    input_string = input()
    if input_string == "q":
        print("I quit")
        exit()

    if input_string == "help":
        return "help"

    if len(input_string) != (4 or 0):
        print("The number must be four digits.")
        correct = False

    if input_string != "" and input_string[0] == '0':
        print("The number must not start with zero.")
        correct = False

    if not input_string.isdigit():
        print("The number must not contain non-numeric characters.")
        correct = False

    if len(set(input_string)) != len(input_string):
        print("The number must not contain duplicates.")
        correct = False

    if not correct:
        input_string = "illegal data"

    return input_string


def compare_numbers(secret_number, guess, count, start_time):
    bulls = 0
    cows = 0

    for i in range(len(secret_number)):
        if secret_number[i] == guess[i]:
            bulls += 1
        elif guess[i] in secret_number:
            cows += 1

    output = ""
    if bulls == 1:
        output += "1 bull"
    else:
        output += f"{bulls} bulls"

    output += ", "
    if cows == 1:
        output += "1 cow"
    else:
        output += f"{cows} cows"

    print(output)

    if bulls == len(secret_number):
        statistics(count, start_time)


def main_bulls_and_cows():
    line_dashes()
    count = 0
    secret_number = guessed_number()
    welcome()
    start_unix_timestamp = time.time()
    while True:
        entry_numbers = input_number()

        if entry_numbers == "help":
            print(secret_number)
            entry_numbers = "illegal data"

        if entry_numbers != "illegal data":
            count += 1
            compare_numbers(secret_number, entry_numbers, count, start_unix_timestamp)


if __name__ == "__main__":
    main_bulls_and_cows()
