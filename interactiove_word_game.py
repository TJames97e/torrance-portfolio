#This will be an interactive python word game 
import random


#Game Name 
word_game_name = 'Fun Word Game'

#Provid Empty Word Bank 
word_bank = []

#Read in the file that contains the words users can guess 
try:
    with open('/Users/eberhart/Python Practice/torrance-portfolio/words.txt') as word_file:
        #print(content)
        for word in word_file:
            word_bank.append(word)
        # print(word_bank)
except FileNotFoundError:
    print("Error: File nnot found")



words_to_guess = random.choice(word_bank)
# print(words_to_guess)

missplaced_location  = []
letters_notin_word = []
maximum_turns = 7
current_turns_taken = 0

print(f'Welcome to {word_game_name}!!')
print('The word has', len(words_to_guess),'letters')
print('You have',maximum_turns-current_turns_taken,'turns left')


