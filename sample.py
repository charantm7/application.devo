import random
from collections import Counter

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split()
word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')

    # Printing the empty spaces for the letters of the word
    print('_ ' * len(word))

    playing = True
    letterGuessed = ''
    chances = len(word) + 2
    flag = False

    try:
        while chances > 0 and not flag:
            print()
            guess = input('Enter a letter to guess: ').lower()

            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue

            letterGuessed += guess

            # Display the word with guessed letters revealed
            for char in word:
                if char in letterGuessed:
                    print(char, end=' ')
                else:
                    print('_', end=' ')
            print()

            # Check if the player has guessed the word correctly
            if Counter(letterGuessed) & Counter(word) == Counter(word):
                print('Congratulations, You won!')
                flag = True
                break

            chances -= 1

        if not flag:
            print('You lost! Try again..')
            print(f'The word was {word}')

    except KeyboardInterrupt:
        print('\nBye! Try again.')
