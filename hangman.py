import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

word_list=['hangman','raistar','whiteff','sanki','munnabhai','godljonathan']
word=random.choice(word_list)
print(word)
print(logo)
lives=6
print(f"*************{lives}/6Lives left***************")
blanks=""

for i in range(len(word)):
    blanks+="_"
print(blanks)
game_over=False
correct_letters=[]
while not game_over:
    guess=input("choose a letter: ").lower()
    
    if guess in correct_letters:
        print(f"you have already entered:{guess}")
    display=""    
    if guess not in word:
        print(f"you guessed {guess} which is not in the word, you lose one life") 
        lives-=1
        print(f"*************{lives}/6Lives left***************")
    if lives==0:
        game_over=True
        print("you lost")
        print(f"it was{word}")
    for letter in word:
        if letter==guess :
            display+=letter
            correct_letters.append(letter)
        elif letter in correct_letters :
            display+=letter
        else:
            display+="_"
    print(display)
    if "_" not in display:
        game_over=True
        print("you win")
    print(stages[lives])    
        