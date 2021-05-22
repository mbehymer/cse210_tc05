from game.console import Console
from game.jumper import Jumper
from game.words import Words
import webbrowser

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        hunter (Hunter): An instance of the class of objects known as Hunter.
        rabbit (Rabbit): An instance of the class of objects known as Rabbit.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.jumper = Jumper()
        self.keep_playing = True
        self.words = Words()
        self.good_guess = True
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
        self.console.write(f'The word was "{self.words.word}".')

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means moving the hunter to a new location.

        Args:
            self (Director): An instance of Director.
        """
        self.console.write(self.words.show_lines() + "\n")
        self.console.write(self.jumper.jumper_output())
        guess = input("Guess a letter [a-z]: ").lower()
        self.good_guess = self.words.get_lines(guess)
        
        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means the rabbit watches the hunter.

        Args:
            self (Director): An instance of Director.
        """
        if self.words.check_for_dashes():
            self.console.write("Great job! We are so proud of you!")
            self.keep_playing = False
        
        if not self.good_guess:
            del self.jumper.jumper_list[0]
            if self.jumper.jumper_list[0] == "   0   ":
                webbrowser.open("https://www.youtube.com/watch?v=oHg5SJYRHA0&ab_channel=cotter548")
                self.keep_playing = False

            
        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the rabbit provides a hint.

        Args:
            self (Director): An instance of Director.
        """
        # hint = self.rabbit.get_hint()
        # self.console.write(hint)
        # self.keep_playing = (self.rabbit.distance[-1] != 0)