class Jumper():

    def __init__(self):
        self.jumper_list = ["  ___  ", " /___\ ", " \   / ", "  \ /  ", "   0   ", "  /|\  ", "  / \  ", " ", "/\\/\\/\\/\\/\\/\\" ] 

    def jumper_output(self):
        jumper_str = ""
        for x in self.jumper_list:
            jumper_str += x + "\n"
        return jumper_str


