#!/usr/bin/python3
"""HBNBCommand Module"""

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB"""
    prompt = "(hbnb)"

    def do_quit(self, args):
        """Quit command to exit the program"""
        return(True)

    def help_quit(self):
        """Help for quit command"""
        print("Quit command to exit the program\n")

    def do_EOF(self, args):
        """EOF command to exit the program"""
        return(True)

    def help_EOF(self):
        """Help for EOF command"""
        print("EOF command to exit the program\n")

    def emptyline(self):
        """If there is no command entered and Return is pressed"""
        pass

    def create(self):
        elif():
            pass

    def show(self):
        pass

    def destroy(self):
        pass

    def all(self):
        pass

    def update(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
