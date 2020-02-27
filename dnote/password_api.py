import os
import random
import string
def generatepass(custom, exclude, charNumber):
    password = ""
    wordlist = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/agwordlist.txt'), 'r').readlines()
    #for line in wordlist:

    #list of seperators used and selection of seperator
    sep = ["-","_",",","."," "]
    sep_used = sep[random.randint(0,len(sep)-1)]

    for element in range(0, len(custom)):
        #upper or lowercase word
        if element == "w":
            password = password + fullwordlist[random.randint(0, count)]
        #Seperator
        elif element == "s":
            password = password + sep_used
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
            password = password + random.choice(string.ascii_letters)
        else: pass
    return password
