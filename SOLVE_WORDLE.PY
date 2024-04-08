import random


words = open('C:/Users/preet/Documents/Python/WORDLE/FIVE_LETTER_WORDS.txt').read().splitlines()


# print(words[:5])


# 1. pick a random word

# 2. make the clue generator

# 3. input next guess

# 4. love life lol

'''
when we think about wordle

i really wanted to solve it using machine learning so i can see the proximity between letters. 
so i guess i have to use reinforcement learning. 

'''

# 1. choose the word
def choose_word(words):
    the_word = random.choice(words)
    return the_word


# print(choose_word(words))


# exploring the zip fucntion

def test_zip_func(the_word,guess):
    for index, (word_letter,guess_letter) in enumerate(zip(the_word,guess)):
        print(index)
        print(word_letter)
        print(type(word_letter))

# test_zip_func("verge","level")

# test_1 = 'reaah'
# test_1 = test_1.replace('a','-',1)

# print(test_1)




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

# print(get_clues("evrge","levee"))
'''
when the expectations are not aligned things are scary. 
like i was scared to walk on the mat with my soocks i was so scared of being yelled at at any given time that i took off my socks. 
but when i saw that my sister litterally wore them on their, i realized i had a misunderstanding of 

'''

# print the clue and the guess nicley



def print_guess_clues(all_guesses, all_clues):
    for thing in zip(all_guesses,all_clues):
        guess_word = thing[0]
        clue = "".join(thing[1])
        print(guess_word, '|',clue)



def play_wordle():
    all_guesses = []
    all_clues = []
    words = open('C:/Users/preet/Documents/Python/WORDLE/FIVE_LETTER_WORDS.txt').read().splitlines()
    the_word = choose_word(words)
    print(the_word)
    guess_num = 0
    while guess_num < 6:
        guess_word = "".join(input("Enter your guess: "))
        if guess_word in words: 
            clue = get_clues(the_word,guess_word)
            all_guesses.append(guess_word)
            all_clues.append(clue)
            print_guess_clues(all_guesses,all_clues)
            guess_num +=1
            if  "".join(clue) == '■■■■■':
                print('Congratulations, you have guessed the word!')
                break
        else:
            print("Please guess a real 5 letter word")
    if guess_num == 6:
        print("The word was ", the_word)

play_wordle()


'''there are a smaller subset of answers and also a smallar subset of possible guesses as well.'''

