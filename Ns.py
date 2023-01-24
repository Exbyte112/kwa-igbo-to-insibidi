import json
import random
# ==================================
# PROGRAM STARTS HERE

sample = "ikpe i kpe ekpere e kpe re"

nsibidi = open("IgbotoNsibidi.json" , encoding="utf8")
nsibidi = json.load(nsibidi)
nsibidi = dict(nsibidi)

randomiser = random.choice(list(nsibidi.keys()))

def userPrompt(result = sample):
    return result
latin_sent = userPrompt() # input any value into the bracket to translate that value or leave it blank to translate a random word

oov = []  # 'oov' stands for 'out of vocabulary', it's a common problem in nlp. This in this list you'll store all your unaccounted for words that don't have a corresponding Nsibidi in your dictionary

nsibidi_sent = []
nsibidi_list = []
for i in latin_sent.split():
    if i not in nsibidi.keys():
        oov.append(i)
    else:
        nsibidi_sent.append(nsibidi[i])
if nsibidi_sent == []:
    print("No words found")
    runner = False
else:
    nsibidi_sent = nsibidi_sent[0]
    runner = True
ans = nsibidi_sent

print(f"These words were not found: {oov}")
print(f"===============\nLATIN: {userPrompt()}\n===============")

def choiceAnswers(ans = latin_sent):
    answer = []
    count = 1
    for i in ans.split():
        previewText = " ".join(answer)
        print(f"Completed: {previewText} ________ ")
        if type(nsibidi[i]) == list:
            print("Choose an answer")
            for j in range(len(nsibidi[i])):
                print(j, nsibidi[i][j])
            ans = int(input("Enter the number of the answer you want: "))
            answer.append(nsibidi[i][ans])
            count += 1
        elif type(nsibidi[i]) == str:
            answer.append(nsibidi[i])
            print("String added")
            count += 1
        else:
            print("error")
            count += 1
    answer = ' '.join(answer)
    return answer

def randomAnswers(ans = latin_sent, ans2 = nsibidi_sent):
    answer = []
    tester = 0
    for i in ans.split():
        if type(nsibidi[i]) == list:
            answer.append(random.choice(nsibidi[i]))
            tester = 0
        elif type(nsibidi[i]) == str:
            answer.append(nsibidi[i])
            tester = 1
        else:
            answer.append("error")
            tester = 2
    return(' '.join(answer) + str(tester))

if runner == True:
    answerGetter = input("Do you want a random answer or a choice based answer? (r/c): ")
    answerGetter = answerGetter.lower() # this converts whichever case to lower
    if answerGetter == "r":
        print("Nsibidi: " + randomAnswers() + "\n=========================\nthis is a random generated result")
    elif answerGetter == "c":
        print("Nsibidi: " + str(choiceAnswers()) + "\n=========================\nthis is a choice based result")
    else:
        print("Invalid input")
else:
    print("No words found")

#============================================
# No longer useful code
"""def randomAnswer(ans = nsibidi_sent):
    if type(nsibidi_sent) == list:
        import random
        ans = random.choice(nsibidi_sent)
        return (' '.join(ans))
    elif type(nsibidi_sent) == str:
        return (' '.join(ans))"""

"""def choiceAnswer(ans = nsibidi_sent):
    #instead of picking a random answer this will ask the user what answer they want
    if type(nsibidi_sent) == list:
        print("Choose an answer")
        for i in range(len(nsibidi_sent)):
            print(i, nsibidi_sent[i])
        ans = int(input("Enter the number of the answer you want: "))
        return (' '.join(nsibidi_sent[ans]))
    else:
        return(' '.join(nsibidi_sent))"""


