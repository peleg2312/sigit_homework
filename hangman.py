


HANGMAN_ASCII_ART = """Welcome to the game Hangman
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/"""
MAX_TRIES = 6
HANGMAN_PHOTOS = {"""x-------x""":0, """    x-------x
    |
    |
    |
    |
    |""":1,"""    x-------x
    |       |
    |       0
    |
    |
    |""":2,"""    x-------x
    |       |
    |       0
    |       |
    |
    |""":3,"""    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""":4,"""    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""":5,"""    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |""":6}


def try_update_letter_guessed(letter_guessed,old_letter_guessed):
    """input: str letter_gussed, list old_letter_guessed
    output: print on screen data and return True or False bassed on if valid or not"""
    if(is_valid_input(letter_guessed,old_letter_guessed)):
        old_letter_guessed.append(letter_guessed)
        return True
    else:
        print("X")
        print(*sorted(old_letter_guessed),sep=" -> ")
        return False

def is_valid_input(letter_guessed,old_letter_guessed):
    """input: str letter_gussed, list old_letter_guessed
    output: return True if valid or False if not"""
    if(letter_guessed.isalpha() and len(letter_guessed)==1 and letter_guessed not in old_letter_guessed):
        return True
    return False

def show_hidden_word(secret_word, old_letter_guessed):
    """input: str secret_word, list old_letter_guessed
    output: print on screen the secret word with only the guessed letters"""
    for char in secret_word:
        if char in old_letter_guessed:
            print(' ' + char + ' ')
        else:
            print(' _ ')
            
def check_win(secret_word,old_letters_guessed):
    """input: str secret_word, list letters_guessed
    output: return True if game won or False if not"""
    #checking by if every char in secret word inside old_letter_guessed
    for char in secret_word:
        if(char not in old_letters_guessed):
            return False
    return True

def print_hangman(num_of_tries):
    """input: int num_of_tries
    output: print the current HANGMAN photo"""
    print(HANGMAN_PHOTOS.get(num_of_tries))
    
    
def choose_word(file_path, index):
    """input: str file_path, int index
    output:return the secret_word choosen"""    
    with open(file_path, 'r') as f:
        list_of_words = f.read().split()
    return list_of_words[index]

def main():

    print(HANGMAN_ASCII_ART, "\n" , MAX_TRIES)
    
    file_path = input("Please enter file path")
    index_of_word = input("Enter the location of a word")
    
    secret_word = choose_word(file_path,index_of_word)
    num_of_tries = 0
    old_letter_guessed = []
    
    while(not check_win(secret_word,old_letter_guessed) or num_of_tries >= MAX_TRIES):
        print_hangman(num_of_tries)
        show_hidden_word(secret_word,old_letter_guessed)
        letter_guessed = input("Guess a letter: ").lower()
        while(try_update_letter_guessed(letter_guessed,old_letter_guessed) == False):
            letter_guessed = input("Guess a letter: ").lower()
        if letter_guessed not in secret_word:
            print("):")
            num_of_tries+=1
            print_hangman(num_of_tries)
        show_hidden_word(secret_word,old_letter_guessed)
            
    if(check_win(secret_word,old_letter_guessed)):
        print("WIN")
    else:
        print("LOSE")
        
        
if __name__ == "__main__":
    main()
    


