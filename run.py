import random
from words import words
import string
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

"""
Need to get a random word from words.py for the user to guess. 
"""

def get_valid_word(words):
    word = random.choice(words) # Chooses a random word from the words.py list of words.
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()


"""
Welcome text, username and guide on how to play. 
""" 

print('Welcome to HangMan')
while True:
    name = input("Please enter your name: \n")
    if not name.isalpha():
        print(Fore.RED + "Invalid entry, you need to enter your name.")
        continue
    else:
        break

print('Hello,', name,'it´s time to play HangMan!')

print(Fore.GREEN + 'This is how the game works: \nYou will get a random english word, can be anything.\nYou will have to use letters on your keyboard to find the correct word.\nYou got 7 lives before it is Game Over!')
start = 'Y'
while True:
    start = input(Fore.BLUE + 'Do you understand the rules? (Y/N)\n')
    if start == 'y' or start == 'Y':
        print("Great, lets continue!")
        break
    else:
        if start != 'y' or start != 'Y':
            print(Fore.RED + "You need to type Y/y to continue")
            continue
            
        


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # This defines, what letter the user has guessed.
    print('Alright, it´s time to start guessing')


    """
    We have to state how many chances the user has to guess the right word, a.k.a, lifes.
    """
    lives = 7


    """
    Next we have to let the user guess an answer in the console.
    """

    while len(word_letters) > 0 and lives > 0:
        print(Fore.GREEN + 'You got', lives, Fore.GREEN + 'lives left. You have guessed these letters: ', Fore.BLUE + ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            
            else: # If user is answering the wrong letter, one life is removed.
                lives = lives - 1
                print(Fore.RED + '\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print(Fore.RED + '\nThat letter is already used, try again!')

        else:
            print(Fore.RED + '\nThat is not a valid letter.')
    
    if lives == 0: #When lives reaches 0, the game ends, or if the word was guessed correctly.
        print(Fore.RED + 'Game over, sorry. The word was', word)
    else:
        print(Fore.GREEN + 'Congratulations! You guessed', word, 'and it was correct!!')





hangman()

"""
The game will ask if the user would want to play the game again.
"""
play_again = 'Y'
while True:
    play_again == 'Y' or play_again == 'y'
    play_again = input('Would you like to play again? (Y/N)\n')
    if play_again == 'Y' or play_again == 'y':
        hangman()
    else:
        if play_again != 'Y' or play_again != 'y':
            print(Fore.RED + 'You need to write Y/y to start again')
            continue