# Cyreexcs.
# Type 'pip install randomword' in Terminal to 
# install randomword module (also works offline).
# Type 'pip install Random-Word-Generator' in Terminal.
import randomword
word = randomword.get_random_word()
print('Guess the word Game')

mistake = 0

listOfStars = ["*"]*len(word)
print(listOfStars, 'word contains', len(word), 'letters')

while mistake < 5:
    guessedFromUserLetter = input("Take a guess mf: ").lower()

# In Case the user types more than 1 character
    if len(guessedFromUserLetter) == 1:

        if guessedFromUserLetter in word and guessedFromUserLetter not in listOfStars:
            print(f"correct {guessedFromUserLetter} is in the Secret Word :D")
# In case a word cointains the same letter
# more than once
            for i in range(len(word)):
                if word[i] == guessedFromUserLetter:
                    listOfStars[i] = guessedFromUserLetter

        elif guessedFromUserLetter in listOfStars:
            print(f'{guessedFromUserLetter} has already been chosen, Please choose Another Letter')        

        else:
            print('You are Wrong')
            mistake += 1

        if mistake == 5:
            print(f'You Lost the word was {word}')

        elif "*" not in listOfStars:
            print('word is correct')
            print(f'it/s {word}')

        print("".join(listOfStars))

    else:
        print("Type a single letter please")
