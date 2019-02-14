import random

hangPhrases = ['Tell me more', 'See no evil', 'Have a nice day', 'Do as I say not as I do']
randomNum = random.randint(0,4)
hangQuestion = hangPhrases[randomNum]
saveLetters = []
print(hangQuestion)
for x in hangQuestion:
    saveLetters.append(x)
    print(saveLetters)




