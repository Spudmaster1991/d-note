import os
import random
from random import getrandbits
import string

wordlist = open(os.path.join(os.path.dirname(os.path.abspath(
    __file__)), 'static/agwordlist.txt'), 'r').readlines()

def generatepass(custom, exclude, charNumber):
    password = ""
    # list of seperators used
    sep = ["-", "_", ",", ".", " "]

    # number of times to repeat a certain generation method
    numRepeat = 0

    for index, element in enumerate(custom):
        if element == "*":
            # Need to get the number after the star
            end = index + 1
            while custom[end] in string.digits:
                ++end
            numRepeat = int(custom[index + 1:end])
            # Need to get the char of the operation to perform
            while numRepeat > 0:
                password = password + operations(index - 1)
        elif element in string.digits:
            pass
    return password


def operations(op):
    text = ''
    # upper or lowercase word
    if op == "w":
        text = word()
    # Seperator
    elif op == "s":
        text = seperator()
    # number
    elif op == "n":
        text = number()
    # Random Character
    elif op == "r":
        text = randomChar()
    # Alphanumeric Character
    elif op == "a"
        text = alphanumeric()
    # Special Character
    elif op == "S":
        text = specialChar()
    # Upper or Lowercase Letter
    elif op == "L":
        text = letter()
    else:
        pass
    return text


def word(wordlist):
    if not getrandbits(1):
        word = string.capitalize(
            wordlist[random.randint(0, len(wordlist) - 1)].strip())
    else:
        word = string.lower(
            wordlist[random.randint(0, len(wordlist) - 1)].strip())
    return word


def seperator():
    return sep[random.randint(0, len(sep) - 1)]


def number():
    return random.choice(string.digits)


def randomChar():
    return random.choice(string.ascii_letters + string.digits + string.punctuation)


def alphanumeric():
    return random.choice(string.ascii_letters + string.digits)


def specialChar():
    return random.choice(string.punctuation)


def letter():
    if not getrandbits(1):
        letter = string.upper(random.choice(string.ascii_letters))
    else:
        letter = string.lower(random.choice(string.ascii_letters))
    return letter
