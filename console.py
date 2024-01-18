#!/usr/bin/python3
"""Console module"""

import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This is the HBNBCommand class for the command interpreter.
    It inherits from cmd.Cmd and provides specific commands.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.

        Args:
            arg (str): Any arguments passed to the command.

        Returns:
            bool: True to exit the command loop.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to quit the program at the end of the file.

        Args:
            arg (str): Any arguments passed to the command.

        Returns:
            bool: True to exit the command loop.
        """
        print("")
        return True

    def help_quit(self):
        """Help message for the quit command."""
        print("Quits the program")

    def help_EOF(self):
        """Help message for the EOF command."""
        print("Exits the program when End of File is reached")

    def emptyline(self):
        """Do nothing on an empty line + ENTER."""
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, save it, and print the id.

        Args:
            arg (str): Class name.

        Returns:
            None
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in {"BaseModel"}:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance.

        Args:
            arg (str): Class name and instance id.

        Returns:
            None
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in {"BaseModel"}:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            instance = all_objects.get(key)
            if instance is None:
                print("** no instance found **")
            else:
                print(instance)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.

        Args:
            arg (str): Class name and instance id.

        Returns:
            None
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in {"BaseModel"}:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            instance = all_objects.get(key)
            if instance is None:
                print("** no instance found **")
            else:
                del all_objects[key]
                storage.save()

    def do_all(self, arg):
        """
        Prints all string representations of instances.

        Args:
            arg (str): Class name (optional).

        Returns:
            None
        """
        args = shlex.split(arg)
        all_objects = storage.all()
        if len(args) == 0:
            print([str(obj) for obj in all_objects.values()])
        elif args[0] not in {"BaseModel"}:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in all_objects.items() if args[0] in key])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id.

        Args:
            arg (str): Class name, instance id, attribute name, and attribute value.

        Returns:
            None
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in {"BaseModel"}:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            instance = all_objects.get(key)
            if instance is None:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                setattr(instance, args[2], args[3])
                instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
