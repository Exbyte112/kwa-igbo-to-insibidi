import json
from os import symlink
import random
from unidecode import unidecode
import os
os.system('cls||clear')
# ==================================
# PROGRAM STARTS HERE

sample = "uba ba uba gwa ba" # This is the sample text (change it to whatever you want)
nsibidi = open("NSdictionary.json" , encoding="utf8") # open the json file
nsibidi = json.load(nsibidi) # load the json file
nsibidi = list(nsibidi) # convert the json file to a list

# collect all the parameters from the dictionary and store them in a list
symList = []
rawProList = []
proList2 = []
formList = []
defsList = []
proList = []

for i in range(len(nsibidi)): # loop through the list
    symList.append(nsibidi[i]["sym"]) # append the sym parameter to the symList
    rawProList.append(nsibidi[i]["pro"]) # append the pro parameter to the proList
    formList.append(nsibidi[i]["form"]) # append the form parameter to the formList
    defsList.append(nsibidi[i]["defs"]) # append the defs parameter to the defsList
# remove all noneType objects from the list
for i in rawProList:
    if i is not None:
        proList.append(i)
    else:
        proList.append("none")
for i in range(len(proList)): # loop through the proList
    if proList[i] is None:
        proList2.append(str("none"))
    else:
        proList2.append(str(unidecode(proList[i])))


# get a random number that's the same length as the list
randomiser = random.randint(0, len(symList)) # get a random number that's the same length as the list (this will be used to get a random word from the dictionary)

def userPrompt(result = sample): # this function gets the user input
    return result

latin_sent = userPrompt() # input any value into the bracket to translate that value or leave it blank to translate a random word

print(f"===============\nLATIN: {userPrompt()}\n===============") # print the user input

def Choice():
    oov = []
    global proList
    global rawProList
    val = []
    for word in sample.split():
        previewText = " ".join(val)
        def chooser(word = word):
            if word in proList:
                return proList.index(word)
            elif word in rawProList:
                return rawProList.index(word)
            else:
                oov.append(word)
                return 0
        indexFinder = chooser()
        def getSym(val = 0): # this function gets the sym value from symList
            return symList[indexFinder + val] # return the random word
        def getPro(val = 0): # this function gets the Pro value from proList
            return proList[indexFinder + val] # return the random word
        def getPro2(val = 0): # this function gets the Pro value from proList
            return proList2[indexFinder + val] # return the random word
        def getForm(val = 0): # this function gets the Form value from formList
            return formList[indexFinder + val] # return the random word
        def getDefs(val = 0): # this function gets the Defs value from defsList
            return defsList[indexFinder + val] # return the random word

        if word in proList:
            count = proList.count(word)
            if count > 1:
                print(f"Completed: {previewText} __________")
                answer = []
                countList = []
                for i in range(count):
                    countList.append(word)
                
                
                print("choose an option: ")
                z = range(count)
                for j in z:
                        pr = proList = [i]
                        print(f"{j} {countList[i]} [{getSym(j)}] ({getDefs(j)})" )
                choice = int(input("Enter your choice: "))
                val.append(getSym())
            elif count == 1:
                val.append(getSym())
            else:
                val.append(getSym())
        elif word in rawProList:
            ans = []
            count = rawProList.count(word)
            if count > 1:
                print(f"Completed: {previewText} __________")
                answer = []
                countList = []
                for i in range(count):
                    countList.append(word)
                print("choose an option: ")
                z = range(count)
                for j in z:
                        pr = rawProList = [i]
                        print(f"{j} {countList[i]} [{getSym(j)}] ({getDefs(j)})" )
                choice = int(input("Enter your choice: "))
                val.append(getSym())
            elif count == 1:
                val.append(getSym())
            else:
                val.append(getSym())
        else:
            if word in proList2:
                rep = input(f"{word} is not recognised, do you mean [{getPro2()}] [{getSym()}] ({getDefs()})? [Y/N]").upper()
                if rep == "Y" or rep == "N":
                    if rep == "Y" or rep == "y":
                        val.append(getSym())
                    else:
                        print("please restart the program")
                else:
                    print("You did not select a valid option")
            elif word in oov:
                rep = input(f"the word seletected [{word}] is not correct, do you want to attempt to translate anyway? [Y/N]").upper()
                if rep == "Y" or rep == "N":
                    if rep == "Y" or rep == "y":
                        val.append(word)
                    else:
                        print("please restart the program")
                else:
                    print("You did not select a valid option")
            else:
                print("entry error")
    return " ".join(val)
    
print(Choice())

