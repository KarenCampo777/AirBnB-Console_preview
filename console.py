#!/usr/bin/python3

"""
Console module.

Entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel


classes = {"BaseModel": BaseModel}

class HBNBCommand(cmd.Cmd):
    """
    HBNB Command prompt - console
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Exit this application
        """
        return True

    def do_EOF(self, arg):
        """
        Exit with EOF (end of file)
        """
        return True

    def emptyline(self):
        """
        Overwritte for not doing anything on empty line
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel.
        Saves it (to the JSON file)
        Prints the id of the new instance

        """
        if not arg:
            print("** class name missing **")
        elif arg not in classes.keys():
            print("** class doesn't exist **")
        else:
            obj = classes[arg]()
            obj.save()
            print(obj.id)

    def do_show():


if __name__ == "__main__":
    HBNBCommand().cmdloop()
