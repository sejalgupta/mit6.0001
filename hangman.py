# Problem Set 2, hangman.py
# Hangman Game

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for word in letters_guessed:
        if word == secret_word:
            return True
    return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    
    lettersList = []
    for i in secret_word:
        lettersList.append('_ ')
    for letter in letters_guessed:
        for i in range(0, len(secret_word)):
            if secret_word[i] == letter:
                lettersList[i] = letter
    return ''.join(lettersList)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    l = list(string.ascii_lowercase)
    for letter in l:
        for guess in letters_guessed:
            if guess == letter:
                l.remove(letter)
    return ''.join(l)
    
def unique_letters(secret_word):    
    '''
    secret_word: string, the secret word to guess.
    
    returns the number of unique letters
    '''
    temp = ""
    for letter in secret_word:
        if letter not in temp:
            temp += letter
    return len(temp)

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    '''
    
    guessRemaining = 6
    guess = []
    uniqueLetters = 0
    warningsLeft = 3
    currentStatus = ""
    
    #tells the user the game, the number of letters in the word, and the number of warnings
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("You have " + str(warningsLeft) + " warnings.")
    print("------------")
    
    #the game component
    while True:
        print("You have " + str(guessRemaining) + " guesses left.") 
        print("Available letters:", get_available_letters(guess))
        letter = input("Please guess a letter: ")
        letter = letter.lower()
        #checks if the letter is lowercase and has not been used
        if letter in string.ascii_lowercase and letter not in guess and letter != "":
            guess.append(letter)
            currentStatus = get_guessed_word(secret_word, guess)
            #if letter is in secret_word, adds one to number of unique letters
            if (letter in currentStatus):
                print("Good guess:", currentStatus)
                uniqueLetters += 1
                #winning condition and end of game
                if (currentStatus.find("_ ") == -1):
                    print("------------")
                    print("Congratulations, you won!")
                    print("Your total score for this game is:", guessRemaining * unique_letters(secret_word))
                    break
            #if letter is not in secret_word
            else:
                print("Oops! That letter is not in my word:", currentStatus)
                if letter in "aeiou":
                    guessRemaining -= 2
                else:
                    guessRemaining -= 1

                
        #checks if the word is input
        elif len(letter) > 1:
            guess.append(letter)
            if is_word_guessed(secret_word, guess):
                print("Good guess:", letter)
                print("------------")
                print("Congratulations, you won!")
                print("Your total score for this game is:", guessRemaining * unique_letters(secret_word))
                break
            else:
                currentStatus = get_guessed_word(secret_word, guess)
                print("Oops! That word is not my word:", currentStatus)
                guessRemaining -= 1
        
        #if input is not a lowercase letter or has been used
        else:
            if letter not in string.ascii_lowercase or letter == "":
                print("Oops! That is not a valid letter.")
            elif letter in guess: 
                print("Oops! You've already guessed that letter.")
            #if warnings are more than 0
            if warningsLeft > 0:
                warningsLeft -= 1
                print("You have", warningsLeft, "warnings left:", currentStatus)
            #if warnings are less than 1
            else: 
                guessRemaining-= 1
                print("You have no warnings left so you lose one guess:", currentStatus)
        
        print("------------")
        
        #lose game condition and end of game
        if (guessRemaining == 0):
            print("Sorry, you ran out of guesses. The word was", secret_word + ".")
            break

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my = my_word.replace(" ", "")
    lettersPrinted = []
    lettersSkipped = []
    if len(my) == len(other_word):
        for i in range(0, len(my)):
            if my[i] == other_word[i] and my[i] not in lettersSkipped:
                if my[i] not in lettersPrinted:
                    lettersPrinted.append(my[i])
                continue
            elif my[i] == "_" and other_word[i] not in lettersPrinted:
                if other_word[i] not in lettersSkipped:
                    lettersSkipped.append(other_word[i])
                continue
            else:
                return False
        return True
    else:
        return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matches = ""
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matches += (word + " ")
            
    if len(matches) > 0:
        return matches
    else:
        return "No matches found"


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessRemaining = 6
    guess = []
    uniqueLetters = 0
    warningsLeft = 3
    currentStatus = ""
    
    #tells the user the game, the number of letters in the word, and the number of warnings
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("You have " + str(warningsLeft) + " warnings.")
    print("------------")
    
    #the game component
    while True:
        print("You have " + str(guessRemaining) + " guesses left.") 
        print("Available letters:", get_available_letters(guess))
        letter = input("Please guess a letter: ")
        letter = letter.lower()
        
        #hint
        if letter == "*":
            currentStatus = get_guessed_word(secret_word, guess)
            print("Possible word matches are:", show_possible_matches(currentStatus))
        
        #checks if the letter is lowercase and has not been used
        elif letter in string.ascii_lowercase and letter not in guess and letter != "":
            guess.append(letter)
            currentStatus = get_guessed_word(secret_word, guess)
            #if letter is in secret_word, adds one to number of unique letters
            if (letter in currentStatus):
                print("Good guess:", currentStatus)
                uniqueLetters += 1
                #winning condition and end of game
                if (currentStatus.find("_ ") == -1):
                    print("------------")
                    print("Congratulations, you won!")
                    print("Your total score for this game is:", guessRemaining * unique_letters(secret_word))
                    break
            #if letter is not in secret_word
            else:
                print("Oops! That letter is not in my word:", currentStatus)
                if letter in "aeiou":
                    guessRemaining -= 2
                else:
                    guessRemaining -= 1

                
        #checks if the word is input
        elif len(letter) > 1:
            guess.append(letter)
            if is_word_guessed(secret_word, guess):
                print("Good guess:", letter)
                print("------------")
                print("Congratulations, you won!")
                print("Your total score for this game is:", guessRemaining * unique_letters(secret_word))
                break
            else:
                currentStatus = get_guessed_word(secret_word, guess)
                print("Oops! That word is not my word:", currentStatus)
                guessRemaining -= 1
        
        #if input is not a lowercase letter or has been used
        else:
            if letter not in string.ascii_lowercase or letter == "":
                print("Oops! That is not a valid letter.")
            elif letter in guess: 
                print("Oops! You've already guessed that letter.")
            #if warnings are more than 0
            if warningsLeft > 0:
                warningsLeft -= 1
                print("You have", warningsLeft, "warnings left:", currentStatus)
            #if warnings are less than 1
            else: 
                guessRemaining-= 1
                print("You have no warnings left so you lose one guess:", currentStatus)
        
        print("------------")
        
        #lose game condition and end of game
        if (guessRemaining == 0):
            print("Sorry, you ran out of guesses. The word was", secret_word + ".")
            break



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = "apple" #choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
