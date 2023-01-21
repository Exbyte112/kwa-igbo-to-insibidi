import json

"""f = open("IgbotoNsibidi2.json") # an edited json file i made with accents removed
words = json.load(f)
words = dict(words)

f2 = open("IgbotoNsibidi2.json") # the original json file u sent to me
words2 = json.load(f2)
words2 = dict(words2)

#print(words)
indeX = 1
nS = words.keys() # the words list in Latin Igbo script
Ig = words.values() # the words list in Nsibidi script

nS2 = words2.keys() # the words list in Latin Igbo script
Ig2 = words2.values() # the words list in Nsibidi script

text = "Na mbu Chineke kere elu  igwe na uwa. Uwa we buru ihe tọb͕ọrọ n'efu na ihe tọb͕ọrọ nkití; ọchichiri di kwa n'elu ob͕u  miri: Mọ Chineke nērughari kwa n'elu miri. Chineke we si, Ka ihè di: ìhè we di. Chineke we hu ìhè ahu, na ọ di nma: Chineke we kpa ókè n'etiti ìhè ahu na ọchichiri ahu. Chineke we kpọ ìhè ahu Ehihie, ọchichiri ahu ka Ọ kpọkwara Abali. Anyasi we di, ututu we di, buru otù ubọchi.Chineke we si, Ka mbara di n'ab͕ata miri ahu, ka ọ nọ kwa nākpa ókè n'etiti miri na miri. Chineke we me mbara ahu, kpa ókè n'etiti miri ahu nke di n'okpuru mbara ahu na miri ahu nke di n'elu mbara ahu: ọ we di otú a. Chineke we kpọ mbara ahu Elu  igwe. Anyasi we di, ututu we di, buru ubọchi nke  abua.Chineke we si, Miri ahu nke di n'okpuru elu  igwe, ka achikọta ha n'otù ebe, ka ahú kwa ala  akọrọ: ọ we di otú a. Chineke we kpọ ala  akọrọ ahu Ala; nchikọta miri ahu ka Ọ kpọkwara Oké Osimiri: Chineke we hu na ọ di nma. Chineke we si, Ka ala puputa ahihia ndu, ihe  ọkukú nke nāmiputa nkpuru  ọghigha, osisi mkpuru nke nāmi mkpuru di iche iche, nke mkpuru  ọghi  gha  ya di nime ya, n'elu ala: o we di otú a. Ala we weputa ahihia ndu, ihe  ọkukú nke nāmiputa nkpuru  ọghigha di iche iche, ya na osisi nke nāmi mkpuru di iche iche, nke nkpuru  ọghigha  ya di nime ya: Chineke we hu na ọ di nma. Anyasi we di, ututu we di, buru ubọchi nke  atọ."
""" # all of this is useless for now but i haven't deleted coz it might be useful later on
# ==================================
# PROGRAM STARTS HERE

def userPrompt(result = "bụ"):
    return result
latin_sent = userPrompt() # input any value into the bracket to translate that value or leave it blank to translate the default value ("bụ")
nsibidi = open("IgbotoNsibidi.json" , encoding="utf8")
nsibidi = json.load(nsibidi)
nsibidi = dict(nsibidi)

oov = []  # 'oov' stands for 'out of vocabulary', it's a common problem in nlp. This in this list you'll store all your unaccounted for words that don't have a corresponding Nsibidi in your dictionary

nsibidi_sent = []
nsibidi_list = []
for i in latin_sent.split():
    if i not in nsibidi.keys():
        oov.append(i)
    else:
        nsibidi_sent.append(nsibidi[i])

nsibidi_sent = nsibidi_sent[0]
ans = nsibidi_sent

print(oov)


def randomAnswer(ans = nsibidi_sent):
    if type(nsibidi_sent) == list:
        import random
        ans = random.choice(nsibidi_sent)
        return (' '.join(ans))
    elif type(nsibidi_sent) == str:
        return (' '.join(ans))

def choiceAnswer(ans = nsibidi_sent):
    #instead of picking a random answer this will ask the user what answer they want
    if type(nsibidi_sent) == list:
        print("Choose an answer")
        for i in range(len(nsibidi_sent)):
            print(i, nsibidi_sent[i])
        ans = int(input("Enter the number of the answer you want: "))
        return (' '.join(nsibidi_sent[ans]))

answerGetter = input("Do you want a random answer or a choice based answer? (r/c): ")
answerGetter = answerGetter.lower() # this converts whichever case to lower
if answerGetter == "r":
    print(randomAnswer() + "\n=========================\nthis is a random generated result")
elif answerGetter == "c":
    print(choiceAnswer() + "\n=========================\nthis is a choice based result")