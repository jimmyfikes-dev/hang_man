import random

hangPhrases = ['Tell me more','See no evil','Have a nice day','Do as I say not as I do']
hangPhraseLength = len(hangPhrases)
randomNum = random.randint(0,hangPhraseLength)
hangQuestion = hangPhrases[randomNum]
chances = 7
wrongAnswer = 0
saveLetters = []
#print('Phrase to solve: ' + hangQuestion) 
for x in hangQuestion:
    x.replace(' ','')
    saveLetters.append(x)
    print(saveLetters)
question = input("Please choose a letter: ")
for r in saveLetters:
    if question in saveLetters:
        print('You got one! Congrats!')
        #input('Okay smart guy, please choose another letter.')
        chances-= 1
        print(chances)
        print(wrongAnswer)
        break    
    else:
        print('Sorry, ' + question + ' is not one of the letter.')
        #input('Please choose another letter.')
        chances-= 1
        wrongAnswer+= 1
        print(chances)
        print(wrongAnswer)    
        break




