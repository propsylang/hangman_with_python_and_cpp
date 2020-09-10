import random

def print_mojiban(word_ans,letters_guessed):
    ret = ""
    for c in word_ans:
        if c in letters_guessed:
            ret += c
        else:
            ret += "_"
    return ret

print("-----------HANGMAN-------------")
cleared = False
tries = 7
word_ans = "default"
letters_guessed = []
while not cleared and tries > 0:
    inp = input("Type in letter or word:")
    if len(inp) is 1 and inp.isalpha():
        if inp in word_ans:
            print("hit!")
            print_mojiban(word_ans,letters_guessed)
    elif len(inp) is len(word_ans) and inp.isalpha():
        if inp is word_ans:
            cleared = True
        else:
            print("wrong word!")
    else:
        print("invalid input")


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
===RIP===''']


