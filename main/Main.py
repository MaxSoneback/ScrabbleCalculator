from functools import reduce
import re
import os.path
import json
from API import yandex_URI as URI
import requests

# In the game Scrabble each letter has a value. One completed word gives you a score.
#
# Write a program that takes a word as an input and outputs the calculated scrabble score.
#
# Values and Letters:
# 1 - A, E, I, O, U, L, N, R, S, T
# 2 - D, G
# 3 - B, C, M, P
# 4 - F, H, V, W, Y
# 5 - K
# 8 - J, X
# 10 - Q, Z
#
# Example:
# The word "cabbage" gives you a score of 14 (c-3, a-1, b-3, b-3, a-1, g-2, e-1)


def load_word_dict_from_file_or_return_empty():
    my_dict = {}
    if os.path.exists("word_list.json"):
        with open("word_list.json", "r") as json_file:
            my_dict = json.load(json_file)
    return my_dict


def save_word_dict_to_file():
    with open("word_list.json", "w") as json_file:
        json.dump(word_dict, json_file)


def is_string_only_letters(string):
    return re.search("^[a-zA-Z]+$", string)


def calculate_score_of_string(string):
    if string not in word_dict:
        word_dict[string] = reduce(lambda x, y: x + scrabble_dict.get(y, 0), string, 0)
    return word_dict[string]


def decide_action():
    action = -1

    while action not in range(0, 4):
        print(
            'What do you want to do next?\n'
            '0. Try a new word \n'
            '1. Get list of old words \n'
            '2. Save word list to file \n'
            '3. Quit')
        try:
            action = int(input())
        except ValueError:
            action = -1
            print("Please enter a number between 0 and 3")
            input("\n Press Enter to continue...\n")
        return action


def print_string_dict():
    for key in word_dict:
        print(f"{key.capitalize()}: {word_dict[key]}")


def check_if_word_exists(word):
    params = {"text": word,
              "lang": "en-en"}
    r = requests.get(url=URI, params=params)
    data = r.json()
    if data["def"]:
        return True
    return False


def main():
    next_action = -1
    word = ""

    while next_action == -1:
        next_action = decide_action()

        if next_action == 0:
            word = ""

        elif next_action == 1:
            print_string_dict()
            input("\n Press Enter to continue...\n")
            next_action = -1

        elif next_action == 2:
            save_word_dict_to_file()
            print("Saved!")
            input("\n Press Enter to continue...\n")
            next_action = -1

        while not word and next_action == 0:
            print("Enter a word to calculate the points it would give in Scrabble: ")
            word = input()
            word = word.strip().lower()

            if is_string_only_letters(word):
                word_exists = check_if_word_exists(word)

                if not word_exists:
                    continuation_choice = -1
                    while continuation_choice not in ('y', 'n', 'Y', 'N'):
                        continuation_choice = input(f"According to Yandex Dictionary, the word '{word.capitalize()}' does not exist, do you want to continue? Y/N:\n")

                        if continuation_choice in ('y', 'Y'):
                            word_exists = True

                        elif continuation_choice in ('n', 'N'):
                            next_action = -1

                        else:
                            continuation_choice = -1

                if word_exists:
                    score = calculate_score_of_string(word)

                    print(f"The total score for '{word.capitalize()}' is {score}")
                    next_action = -1

            else:
                print("The word can only contain letters from A-Z, please try again")
                input("\n Press Enter to continue...\n")
                word = ""


word_dict = load_word_dict_from_file_or_return_empty()
scrabble_dict = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1,
                         "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1, "s": 1, "t": 1, "u": 1, "v": 4, "w": 4,
                         "x": 8, "y": 4, "z": 10}
main()
