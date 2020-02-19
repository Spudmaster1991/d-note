import random
import string
def generatepass(custom, wordlist, seperators, customChar, numbers, specialChar, exclude, letters):
    password = ""
    #import wordlist
    wordlist = 'C:/Users/Anthony/Documents/GitHub/password_reset/static/agwordlist.txt'
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
            #Random Charecter
            elif element == "r":
                password = password + random.choice(string.printable)
            #Special Charecter
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
    elif wordlist == True & numbers == True & specialChar == True:
        pass
    elif wordlist == True & numbers == True & specialChar == False:
        pass
    elif wordlist == True & numbers == False & specialChar == True:
        pass
    elif wordlist == True & numbers == False & specialChar == False:
        pass
    elif wordlist == False & numbers == True & specialChar == True:
        pass
    elif wordlist == False & numbers == True & specialChar == False:
        pass
    elif wordlist == False & numbers == False & specialChar == True:
        pass
    elif wordlist == False & numbers == False & specialChar == False:
        pass
    # wordlist = 'C:/Users/Anthony/Documents/GitHub/password_reset/static/agwordlist.txt'
    # count = len(open(wordlist).readlines(  ))
    # with open(wordlist) as wl:
    #     fullwordlist = wl.read().split('\n')
    #     wl.close()    
    # word1 = fullwordlist[random.randint(0, count)]
    # word2 = fullwordlist[random.randint(0, count)]
    # word3 = fullwordlist[random.randint(0, count)]

    # seperators = ['.', '-', '*', '"']

    # password = word1 + str(random.randint(0, 9)) + seperators[random.randint(0, 3)] + word2 + str(random.randint(0, 9)) + seperators[random.randint(0, 3)] + word3 + str(random.randint(0, 9))
    # return(password)
