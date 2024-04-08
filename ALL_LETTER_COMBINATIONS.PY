from itertools import product
import random


# Define the set of letters
letters = 'abcdefghijklmnopqrstuvwxyz'

# Generate all possible 5-letter combinations
combinations = [''.join(combination) for combination in product(letters, repeat=5)]



def choose_word(words):
    the_word = random.choice(words)
    return the_word






def get_clues(the_word,guess):
    clue = ["-"] * len(the_word)
    for index,(word_letter,guess_letter) in enumerate(zip(the_word,guess)):
        if guess_letter == word_letter:
            clue[index] = "■"
            the_word = the_word.replace(guess_letter,'-',1)
    for index,(word_letter,guess_letter) in enumerate(zip(the_word,guess)):
        if guess_letter in the_word and clue[index] == "-":
            clue[index] = "□"
            the_word = the_word.replace(guess_letter,'-',1)


    return clue



def print_guess_clues(all_guesses, all_clues):
    for thing in zip(all_guesses,all_clues):
        guess_word = thing[0]
        clue = "".join(thing[1])
        print(guess_word, '|',clue)





def play_wordle():
    all_guesses = []
    all_clues = []
    words = [''.join(combination) for combination in product(letters, repeat=5)]
    the_word = choose_word(words)
    print(the_word)
    guess_num = 0
    while guess_num < 6:
        guess_word = "".join(input("Enter your guess: "))
        if len(guess_word) == 5: 
            clue = get_clues(the_word,guess_word)
            all_guesses.append(guess_word)
            all_clues.append(clue)
            print_guess_clues(all_guesses,all_clues)
            guess_num +=1
            if  "".join(clue) == '■■■■■':
                print('Congratulations, you have guessed the word!')
                break
        else:
            print("Please guess a real 5 code")
    if guess_num == 6:
        print("The word was ", the_word)

play_wordle()



''' we can allow any letters in th guess, for example, like in wordel we can allow aaaaa as a possible word
and then ??? or should i just use reinforcement learning???




'''