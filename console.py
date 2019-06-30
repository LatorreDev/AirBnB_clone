#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """Interpeter"""
    prompt = "(hbnb)"

    def do_quit(self, args):
        """exit interpeter"""
        return True
    def do_EOF(self, args):
        """exit interpeter"""
        return True
if __name__ == '__main__':
    MY_INTERPETER = HBNBCommand()
    MY_INTERPETER.cmdloop()
