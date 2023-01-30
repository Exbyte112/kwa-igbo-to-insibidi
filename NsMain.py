import json
from os import symlink
import random
from unidecode import unidecode
# ==================================
# PROGRAM STARTS HERE

sample = "chü" # This is the sample text (change it to whatever you want)

nsibidi = open("NSdictionary.json" , encoding="utf8") # open the json file
nsibidi = json.load(nsibidi) # load the json file
nsibidi = list(nsibidi) # convert the json file to a list

# collect all the parameters from the dictionary and store them in a list
symList = []
proList = []
proList2 = []
formList = []
defsList = []

for i in range(len(nsibidi)): # loop through the list
    symList.append(nsibidi[i]["sym"]) # append the sym parameter to the symList
    proList.append(nsibidi[i]["pro"]) # append the pro parameter to the proList
    formList.append(nsibidi[i]["form"]) # append the form parameter to the formList
    defsList.append(nsibidi[i]["defs"]) # append the defs parameter to the defsList
for i in range(len(proList)): # loop through the proList
    if type(proList[i]) != str:
        proList2.append("None")
    else:
        proList2.append(unidecode(proList[i]))

# get a random number that's the same length as the list
randomiser = random.randint(0, len(symList)) # get a random number that's the same length as the list (this will be used to get a random word from the dictionary)

def userPrompt(result = sample): # this function gets the user input
    return result

latin_sent = userPrompt() # input any value into the bracket to translate that value or leave it blank to translate a random word

print(f"===============\nLATIN: {userPrompt()}\n===============") # print the user input

def getSym(): # this function gets the sym value from symList
    return symList[randomiser] # return the random word
def getPro(): # this function gets the Pro value from proList
    return proList[proList.index(latin_sent)] # return the random word
def getPro2(): # this function gets the Pro value from proList
    return proList2[randomiser] # return the random word
def getForm(): # this function gets the Form value from formList
    return formList[randomiser] # return the random word
def getDefs(): # this function gets the Defs value from defsList
    return defsList[randomiser] # return the random word

def randomWord(): # this function gets a random word from the dictionary
    return f"Sym: {getSym()}\nPro: {getPro2()}\nForm: {getForm()}\nDefs: {getDefs()}\nPosition: {(randomiser*6)+3}" # return the random word




print(f"===============\nNSIBIDI: {randomWord()}\n===============") # print the random word
