import random

hangPhrases = ['Tell me more','See no evil','Have a nice day','Do as I say not as I do']
hangPhraseLength = len(hangPhrases)
randomNum = random.randint(0,hangPhraseLength)
hangQuestion = hangPhrases[randomNum]
chances = 7
wrongAnswer = 0
saveLetters = []

def lessChances():
    chances-= 1
    print("Chances left: " + chances)


def pickLetter():
    print('You got one! Congrats!')
    

def pickAnotherLetter():
    input('Please pick another letter')
    lessChances()

def pickLetterSuccess():
    correctAns = input('Okay smart guy, please choose another letter.')
    if correctAns in saveLetters:
            print("Wow, you got another one")
            print(chances)
            pickAnotherLetter()
    else:
            print("Sorry, you got that one wrong buddy.")
            pickAnotherLetter()

for x in hangQuestion:
    x.replace(' ','')
    saveLetters.append(x)
    print(saveLetters)
question = input("Please choose a letter: ")
for r in saveLetters:
    if question in saveLetters:
        pickLetter()
        pickLetterSuccess()           
        print(wrongAnswer)
        break    
    else:
        print('Sorry, ' + question + ' is not one of the letter.')
        wrongAns = input('Please choose another letter.')
        wrongAnswer+= 1
        print(chances)
        print(wrongAnswer)    
        break




