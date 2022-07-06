import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  

    lives = 7

    
    while len(word_letters) > 0 and lives > 0:
     
        print('Mas', lives, 'zivotou a skusal si: ', ' '.join(used_letters))

        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Slovo: ', ' '.join(word_list))

        user_letter = input('Hadaj: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1  
                print('Pismeno,', user_letter, 'tam nepatri')

        elif user_letter in used_letters:
            print('To uz si pouzil')

        else:
            print('Pismena mas hadat')

    if lives == 0:
        print('Sorry umrel si bolo to', word)
    else:
        print('Dal si to', word, '!!')


hangman()
