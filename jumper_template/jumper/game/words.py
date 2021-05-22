import random

class Words():
    """A code template for a list of words.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        jumper (Jumper): An instance of the class of objects known as Jumper.
        words (Words): An instance of the class of objects known as Words.
    """
    

    def __init__(self):
        """The words class constructor.
        
        Args:
            self (words): an instance of words.
        """
        self.word_list = self.__load_words()
        self.word = self.get_word()
        self.current_word = [ "_" for x in range(len(self.word))]

    def __load_words(self):
        """
        Loads the word file into a list and returns it. 
        """
        with open("jumper_template/jumper/game/words.txt") as word_list:
            word_list = word_list.read()
            word_list = word_list.split()
        
        return word_list

    def get_word(self):
        """Get a random word from the list"""

        return random.choice(self.word_list)

    def show_lines(self):
        """returns a string with the number of characters """
        lines = ""
        for x in self.current_word:
            lines += x + " "
        return lines


    def get_lines(self, guess):
        """ Updates the current word with the correct guess."""
        if guess in self.word:
            
            for i in range(len(self.word)):
                if guess == self.word[i]:
                    self.current_word[i] = guess
            return True
        else:
            return False
    
    def check_for_dashes(self):
        """Checks for dashes"""

        if not "_" in self.current_word:
            return True
        else:
            return False