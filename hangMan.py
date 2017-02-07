'''
Created on Sep 15, 2016
@author: kiwis
'''
import theDictionary, random
words_list = theDictionary.dic

hangmanPics = ['''
    +------|
    |      |
           |
           |
           |
           |
           |
=============''','''
    +------|
    |      |
    0      |
           |
           |
           |
           |
=============''','''
    +------|
    |      |
    0      |
    |      |
           |
           |
           |
=============''','''
    +------|
    |      |
    0      |
    |      |
    |      |
           |
           |
=============''','''
    +------|
    |      |
    0      |
   /|      |
    |      |
           |
           |
=============''','''
    +------|
    |      |
    0      |
   /|\     |
    |      |
           |
           |
=============''','''
    +------|
    |      |
    0      |
   /|\     |
    |      |
   /       |
           |
=============''','''
    +------|
    |      |
    0      |
   /|\     |
    |      |
   / \     |
           |
=============''']


def startsGame():
    var = 'space saver'
    print("SUPER HANGMAN")
    while not(var == ''):
        var = input('Press enter to play hangman')
    var  = 'Space saver'
        

def wordOfLength(x):
    length_list = []
    for i in words_list: 
        if x == len(i):
            length_list.append(i)
    b = random.randint(0, len(length_list))
    return length_list[b]
            
     
def getsWord():
    choice = input("""Please choose a difficulty by entering the corresponding number
    1 - Easy
    2 - Medium
    3 - Hard
    4 - Extreme
    
    ==> """)
    while choice not in '1234':
        print('Please pick a number')
        
    if choice == '1':
        return wordOfLength(5) 
    elif choice == '2':
        return wordOfLength(7) 
    elif choice == '3':
        return wordOfLength(9)
    elif choice == '4':
        return wordOfLength(11)
    
def getGuess(alreadyGuessed):
    while True:
        guess = input('Guess a letter ==> ')
        guess = guess.lower()
        
        if len(guess) != 1:
            print('Please enter one letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please guess a fucking LETTER.')
        else: 
            return guess
        
def isGuessRight(secretWord, guess):
    for x in range(0, len(secretWord)):
        if guess == secretWord[x]:
            return True
        else:
            False

#found a way around this
#def findIndex(secretWord, guess):
    #return [i for i, letter in enumerate(secretWord) if letter == guess]

def displaysBoards(hangmanPics, missedLetters, correctLetters, secretWord):
    
    print(hangmanPics[len(missedLetters)] + '\n')
    
    print('Incorrect guesses: ' + ' '.join(missedLetters + '\n'))
    
    blanks = '_' * len(secretWord)
    for x in range(len(secretWord)):
        if secretWord[x] in correctLetters:
            blanks = blanks[:x] + secretWord[x] + blanks[x + 1:]
    
    for letter in blanks:
        print(letter, end=' ')


def playAgain():
    choice = input('Would you like to play again? (yes/no) ==>')
    print('')
    return choice.lower().startswith('y')


startsGame()
missedLetters = ''
correctLetters = ''
secretWord = getsWord()
gameIsOver = False


while True:
    displaysBoards(hangmanPics, missedLetters, correctLetters, secretWord)
    print('\n')
    #print(secretWord)
    guess = getGuess(missedLetters + correctLetters)
    
    if isGuessRight(secretWord, guess):
        correctLetters = correctLetters + guess
        print('Correct!')
        
        youWon = True
        for x in range(len(secretWord)):
            if secretWord[x] not in correctLetters:
                youWon = False
                break
        if youWon:
            print('\n' + 'Congratulations! The word is ' + secretWord+'.')
            gameIsOver = True
    else:
        missedLetters = missedLetters + guess
        
        if len(missedLetters) == 7:
            displaysBoards(hangmanPics, missedLetters, correctLetters, secretWord)
            print('You Lose! You Died!\n' + 'The word was ' + secretWord)
            gameIsOver = True
    
    if gameIsOver:
        if playAgain():
            startsGame()
            missedLetters = ''
            correctLetters = ''
            print('it worked')
            gameIsOver = False
            secretWord = getsWord()
        else:
            break
