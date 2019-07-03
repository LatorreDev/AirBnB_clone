#!/usr/bin/python3
"""HBNBCommand Module"""

import cmd
import sys
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB"""
    prompt = "(hbnb)"


    def do_quit(self, args):
        """Quit command to exit the program"""
        return(True)

    def help_quit(self):
        """Help for quit command"""
        print("Quit command to exit the program\n")

    def do_EOF(self):
        """EOF command to exit the program"""
        return(True)

    def help_EOF(self):
        """Help for EOF command"""
        print("EOF command to exit the program\n")

    def emptyline(self):
        """If there is no command entered and Return is pressed"""
        pass

    def do_create(self, args):
        my_list = ["User", "City", "Amenity", "Name", "Place", "Review", "BaseModel"]
        arg_eval = (args.split())
        if len(arg_eval) == 0:
            print("** class name missing **")
        elif arg_eval[0] in my_list:
            new_obj = eval(arg_eval[0])(arg_eval[1:])
            print(new_obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self):
        pass

    def do_destroy(self):
        pass

    def do_all(self):
        pass

    def do_update(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
