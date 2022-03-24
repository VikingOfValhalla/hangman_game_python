##########################################################
'''
                Author: VikingOfValhalla
                    Date: 12/27/2021
                Email: Tom.Wilson@nordtechsystems.com
'''
##########################################################


from hangman_board import *

from random_word import *

print(hangman_board[5])



word = word_index

word_hidden = "_" * len(word)
print(word_hidden, "\n")

class Hangman(object):
    def __init__(self, word, word_hidden):
        self.word = word
        self.word_hidden = word_hidden
        self.attempts = attempts
    
    def guess_word(word_hidden):
        '''
        input letter, replace underscores in word_hidden with 
        selected letter for corresponding position
        '''

        try:
            attempts = 5
            while attempts > 0:

                player_input = input("Please select ONE letter: ")[0].lower()    
                
                for letter in player_input:
                    if (player_input.isalpha()) == False:
                        print("WARNING: Please select only letters")  
                    '''
                    if player_input.count(letter) > 1:
                        print("Please select one character at a time.")
                        break
                    '''
                            
                if player_input in word:
                    def find_duplicates(word, player_input):
                        '''
                        input letter, find all positions of that letter within the word
                        '''
                        return [i for i, letter in enumerate(word) if letter == player_input]
                        
                    duplicate_pos = find_duplicates(word, player_input)
                    
                    for element in duplicate_pos:
                        element_int = element
                        word_hidden = word_hidden[:element_int] + player_input + word_hidden[element_int + 1:]
                    
                if player_input not in word:
                    attempts = attempts - 1
                    print(hangman_board[attempts])

                if attempts == 0:
                    print(hangman_board[0])
                    print(word)

                if "_" not in word_hidden:
                    print("\nYou Win!\n")
                    break
                
                        
                print(word_hidden, "Attempts Left: ", attempts, "\n")

        except Exception as e:
            print(e)
    
    guess_word(word_hidden)

