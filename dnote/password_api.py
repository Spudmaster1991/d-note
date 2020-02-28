import os
import random
from random import getrandbits
import string
def generatepass(custom, exclude, charNumber):
    password = ""
    wordlist = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/agwordlist.txt'), 'r').readlines()

    #list of seperators used
    sep = ["-","_",",","."," "]
    previousChar = ''

    for element in custom:
        previousChar = element
        #upper or lowercase word
        if element == "w":
            if not getrandbits(1):
                word = string.capitalize(wordlist[random.randint(0, len(wordlist) - 1)].strip())
            else:
                word = string.lower(wordlist[random.randint(0, len(wordlist) - 1)].strip())
            password = password + word
        #Seperator
        elif element == "s":
            password = password + sep[random.randint(0,len(sep) - 1)]
        #number
        elif element == "n":
            password = password + random.choice(string.digits)
        #Random Character
        elif element == "r":
            password = password + random.choice(string.printable)
        #Special Character
        elif element == "S":
            password = password + random.choice(string.punctuation)
        #Upper or Lowercase Letter
        elif element == "L":
            if not getrandbits(1):
                letter = string.upper(random.choice(string.ascii_letters))
            else:
                letter = string.lower(random.choice(string.ascii_letters))
            password = password + letter
        else: pass

    return password
