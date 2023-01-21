import json

f = open("IgbotoNsibidi2.json") # an edited json file i made with accents removed
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

Finaltext = text.split() # convert the text entered to a list of words so i can loop through it'd values

"""print(words["ụrụ"]+ " hello")""" # this is useless as i use it to keep track of what the keys do


li = ""
for word in Finaltext:
    if word in nS: # check if the word in the text is in the list of words from the original json file
        o = words[word]
        o = str(o)
        li+= o # add the word to the list
    elif word in nS2: # check if the word in the text is in the list of words from the edited json file
        o = words2[word]
        o = str(o)
        li+= o # add the word to the list

print(li) # print the list of words collected

