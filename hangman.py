import random

def printword_with_holes():
    pass

print("-----------HANGMAN-------------")
cleared = False
tries = 7
word_ans = "default"
letters_guessed = []
while not cleared and tries > 0:
    inp = input("Type in letter or word:").upper()
    if len(inp) is 1 and inp.isalpha():
        if inp in word_ans:
            pass
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


