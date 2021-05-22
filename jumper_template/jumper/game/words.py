import random

class Words():
    

    def __init__(self):
        self.word_list = self.__load_words()
        self.word = self.get_word()
        # self.word = "apple"
        self.current_word = [ "_" for x in range(len(self.word))]

    def __load_words(self):
        with open("jumper_template/jumper/game/words.txt") as word_list:
            word_list = word_list.read()
            word_list = word_list.split()
        
        return word_list

    def get_word(self):
        """Get a random word from the list"""

        return random.choice(self.word_list)

    def show_lines(self):
        lines = ""
        for x in self.current_word:
            lines += x + " "
        return lines


    def get_lines(self, guess):
        if guess in self.word:
            
            for i in range(len(self.word)):
                if guess == self.word[i]:
                    self.current_word[i] = guess
            return True
        else:
            return False
    
    def check_for_dashes(self):
        """Read previous line"""

        if not "_" in self.current_word:
            return True
        else:
            return False
            
        
        
        

# words = Words()
# for x in words.current_word:
#     print(x, end=" ")
# print()
# guess =""
# while guess != "quit":
#     guess = input("What's your guess? ")
#     words.get_lines(guess)
#     for x in words.current_word:
#         print(x, end=" ")
#     print()