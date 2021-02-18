#!/usr/bin/python3
"""
 cmd
"""

from models.base_model import BaseModel
import cmd
import sys
import os


class HBNBCommand(cmd.Cmd):
    """
    hbm implementation
    Args:
        cmd ([type]): [description]
    """
    Models = {"BaseModel": BaseModel}
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """ Exit method for EOF """
        print('')
        exit()

    def do_help(self, args):
        """Get help on commands
        """
        cmd.Cmd.do_help(self, args)

    def do_quit(self, arg):
        """ Exit method """
        exit()

    def do_create(self, args):
        """[summary]

        Args:
            args ([model]): [description]
        """
        if args == "":
            print("** class name missing **")
        elif args not in self.Models:
            print("** class doesn't exist **")
        else:
            model = self.Models[args]()
            model.save()
            print(model.id)

    def do_show(self, arg):
        """[summary]

        Args:
            arg ([type]): [description]
        """
        print(arg.split(" "))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
