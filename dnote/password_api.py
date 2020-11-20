import os
import random
from random import getrandbits
import string

wordlist = open(os.path.join(os.path.dirname(os.path.abspath(
    __file__)), 'static/agwordlist.txt'), 'r').readlines()
# list of seperators used
sep = ["-", "_", ",", "."]
randomSeperator = sep[random.randint(0, len(sep) - 1)]

def generatepass(custom, exclude, charNumber):
    password = ""
    # number of times to repeat a certain generation method
    numRepeat = 0

    for index, element in enumerate(custom):
        if element == "*":
            # Need to get the number after the star
            end = index + 1
            try:
                while custom[end] in string.digits:
                    end = end + 1
            except:
                pass
            finally:
                # Need to get the char of the operation to perform
                numRepeat = int(custom[index + 1:end])

                # Set limit how many times it can repeat
                if numRepeat > 100:
                    numRepeat = 100

                # while loop starts at one because one operation happened already
                while numRepeat > 1:
                    numRepeat = numRepeat - 1
                    password = password + operations(custom[index - 1])
        elif element in string.digits:
            pass
        else:
            password = password + operations(element)
    return password


def operations(op):
    text = ''
    # Uppercase word
    if op == "W":
        text = upperWord()
    elif op == "w"
        text = lowerWord()
    # Seperator
    elif op == "s":
        text = seperator()
    # number
    elif op == "n":
        text = number()
    # Random character
    elif op == "r":
        text = randomChar()
    # Alphanumeric character
    elif op == "a":
        text = alphanumeric()
    # Special character
    elif op == "S":
        text = specialChar()
    # Lowercase letter
    elif op == "l":
        text = lowerLetter()
    # Uppercase letter
    elif op == "L":
        text = upperLetter()
    else:
        pass
    return text


def upperWord():
    word = string.capitalize(
        wordlist[random.randint(0, len(wordlist) - 1)].strip())
    return word

def lowerWord():
    word = string.lower(
        wordlist[random.randint(0, len(wordlist) - 1)].strip())
    return word

def seperator():
    return randomSeperator

def number():
    return random.choice(string.digits)

def randomChar():
    return random.choice(string.ascii_letters + string.digits + string.punctuation)

def alphanumeric():
    return random.choice(string.ascii_letters + string.digits)

def specialChar():
    return random.choice(string.punctuation)

def lowerLetter():
    letter = string.lower(random.choice(string.ascii_letters))
    return letter

def upperLetter():
    letter = string.upper(random.choice(string.ascii_letters))
    return letter
