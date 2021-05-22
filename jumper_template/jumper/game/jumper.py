class Jumper():
    """Keeps track of the jumper
    
    Stereotype: service provider
        

    Attributes:
        jumper_list: a list that holds the image of the jumper
        
    """
    def __init__(self):
        """Jumper class constructor.
        
        Args:
            self (Jumper): an instance of Jumper.
        """
        self.jumper_list = ["  ___  ", " /___\ ", " \   / ", "  \ /  ", "   0   ", "  /|\  ", "  / \  ", " ", "/\\/\\/\\/\\/\\/\\" ] 

    def jumper_output(self):
        """
        Puts jumper list into a string.
        """
        jumper_str = ""
        for x in self.jumper_list:
            jumper_str += x + "\n"
        return jumper_str


