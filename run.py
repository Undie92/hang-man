import random
from words import words
import string


"""
Need to get a random word from words.py for the user to guess. 
"""

def get_valid_word(words):
    word = random.choice(words) # Chooses a random word from the words.py list of words.
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

print('Welcome to HangMan')


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # This defines, what letter the user has guessed.
    print('Start guessing')


    """
    We have to state how many chances the user has to guess the right word, a.k.a, lifes.
    """
    lives = 5


    """
    Next we have to let the user guess an answer in the console.
    """

    while len(word_letters) > 0 and lives > 0:
        print('You got', lives, 'lives left. You have guessed these letters: ', ' '.join(used_letters))

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
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nThat letter is already used, try again!')

        else:
            print('\nThat is not a valid letter.')
    
    if lives == 0: #When lives reaches 0, the game ends, or if the word was guessed correctly.
        print('Game over, sorry. The word was', word)
    else:
        print('Congratulations! You guessed', word, 'and it was correct!!')





hangman()

"""
The game will ask if the user would want to play the game again.
"""
play_again = 'Y'
while play_again == 'Y' or play_again == 'y':
    play_again = input('Would you like to play again? (Y/N)')
    if play_again == 'Y' or play_again == 'y':
         hangman()