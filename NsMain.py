import json
from os import symlink
import random
from unidecode import unidecode
import os
os.system('cls||clear')
# ==================================
# PROGRAM STARTS HERE

sample = "á:bö á:bökö áböshį ágü" # This is the sample text (change it to whatever you want)
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
    global proList
    global rawProList
    val = []
    for word in sample.split():
        if word in proList:
            indexFinder = proList.index(word)
        else:
            indexFinder = rawProList.index(word)
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
        previewText = " ".join(val)
        if word in proList:
            count = proList.count(word)
            if count > 1:
                answer = []
                countList = []
                for i in range(count):
                    countList.append(word)
                
                print(f"Completed: {previewText} __________")
                print("choose an option: ")
                z = range(count)
                for j in z:
                        pr = proList = [i]
                        print(f"{j} {countList[i]} [{getSym(j)}] ({getDefs(j)})" )
                choice = int(input("Enter your choice: "))
                val.append(countList[choice])
                val.append("from nest if statement")
            elif count == 1:
                val.append(word)
                val.append("from nest elif statement")
            else:
                val.append(word)
                val.append("from nest else statement")
        elif word in rawProList:
            ans = []
            count = rawProList.count(word)
            if count > 1:
                answer = []
                countList = []
                for i in range(count):
                    countList.append(word)
                previewText = " ".join(ans)
                print(f"Completed: {previewText} __________")
                print("choose an option: ")
                z = range(count)
                for j in z:
                        pr = rawProList = [i]
                        print(f"{j} {countList[i]} [{getSym(j)}] ({getDefs(j)})" )
                choice = int(input("Enter your choice: "))
                val.append(countList[choice])
                val.append("from nest if statement")
            elif count == 1:
                val.append(word)
                val.append("from nest elif statement")
            else:
                val.append(word)
                val.append("from nest else statement")
        else:
            val.append(word)
            val.append("from else statement")
    return " ".join(val)
    
print(Choice())

"""def choiceAns():
    #when sample contains a value that has more than one definition, this function will ask the user to choose a definition
    answer = []
    count = 1
    for i in proList:
        previewText = " ".join(answer)
        print(f"Completed: {previewText} __________")
        print("choose an option: ")
        z = range(count)
        for j in z:
                pr = proList = [i]
                print(f"{j} {i}" )"""

def randomWord(): # this function gets a random word from the dictionary
    return f"Sym: {getSym()}\nPro: {getPro2()}\nForm: {getForm()}\nDefs: {getDefs()}\nPosition: {(indexFinder*6)+3}" # return the random word




"""print(f"===============\nNSIBIDI: {randomWord()}\n===============")""" # print the random word
