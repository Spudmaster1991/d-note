import os
import random
import string
def generatepass(custom, wordlist, seperators, customChar, numbers, specialChar, exclude, letters, charNumber):
    password = ""
    wordlist = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/agwordlist.txt')
    count = len(open(wordlist).readlines(  ))
    with open(wordlist) as wl:
        fullwordlist = wl.read().split('\n')
        wl.close()
    #list of seperators used and selection of seperator
    sep = ["-","_",",","."," "]
    sep_used = sep[random.randint(0,len(sep)-1)]


    if custom != "":
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
    #If wordlist is checked make a password with n words
    elif wordlist != "":
        i=0
        while i < wordlist:
            password = password + random.choice(string.digits)
            #If seperators is checked but a sperator every n words
            if seperators != "" & i == seperators-1:
                    password = password + sep_used
            i=+1
            pass
        pass
    elif letters == True & numbers == True & specialChar == True:
        pass
    elif letters == True & numbers == True & specialChar == False:
        pass
    elif letters == True & numbers == False & specialChar == True:
        pass
    elif letters == True & numbers == False & specialChar == False:
        pass
    elif letters == False & numbers == True & specialChar == True:
        pass
    elif letters == False & numbers == True & specialChar == False:
        pass
    elif letters == False & numbers == False & specialChar == True:
        pass
    elif letters == False & numbers == False & specialChar == False:
        pass
    return password
