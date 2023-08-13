#!/usr/bin/python3

"""This is a console"""

import cmd


class HBNBCommand(cmd.Cmd):
    """This defines the entry point of the command interpreter"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Passes simpley upon enter"""
        pass

    def do_quit(self, line):
        """Quit is a modified method. It helps us to exit from the Console."""
        return True

    def do_EOF(self, line):
        """Helps us to exit from the Console."""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
