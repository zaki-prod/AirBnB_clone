#!/usr/bin/python3

"""This is a console"""

import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """This defines the entry point of the command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit is a modified method. It helps us to exit from the Console."""
        return True

    def do_EOF(self, line):
        """Helps us to exit from the Console."""
        print("")
        return True

    def emptyline(self):
        """Passes simpley upon enter"""
        pass

    def do_create(self, line):
        """Creates a new instance"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.allclasses():
            print("** class doesn't exist **")
        else:
            new_instance = storage.allclasses()[line]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints String representation of an instance based
        on the class name and id"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            token = line.split(' ')
            if token[0] not in storage.allclasses():
                print("** class doesn't exist **")
            elif len(token) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(token[0], token[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on
        the class name and id"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            token = line.split(" ")
            if token[0] not in storage.allclasses():
                print("** class doesn't exist **")
            elif len(token) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(token[0], token[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name"""
        if line != "":
            token = line.split(" ")
            if token[0] not in storage.allclasses():
                print("** class doesn't exist **")
            else:
                new_list = []
                for obj in storage.all().values():
                    if type(obj).__name__ == token[0]:
                        new_list.append(str(obj))
                print(new_list)
        else:
            new_list = []
            for obj in storage.all().values():
                new_list.append(str(obj))
            print(new_list)

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""
        token = line.split(' ')

        if line == "" or line is None:
            print("** class name missing **")

        elif token[0] not in storage.allclasses():
            print("** class doesn't exist **")

        elif len(token) < 2:
            print("** instance id missing **")

        elif len(token) < 3:
            print("** attribute name missing **")

        elif len(token) < 4:
            print("** value missing **")

        else:
            key = "{}.{}".format(token[0], token[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                setattr(storage.all()[key], token[2], token[3])
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
