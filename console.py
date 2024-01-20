#!/usr/bin/python3
"""Console module"""
import os
import json
import cmd
import shlex
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
from models.user import User

class HBNBCommand(cmd.Cmd):

    CLASSES = {
    'BaseModel': BaseModel,
    'User': User,}
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

    def do_emptyline(self):
        """Do nothing on an empty line + ENTER."""
        pass

    def do_create(self, args):
        if not args:
            print("** class name missing **")
        elif args[0] not in {"BaseModel", "User"}:
            print("** class doesn't exist **")
        else:
            if args[0] == "User":
                new_instance = User()
            else:
                new_instance = BaseModel()


            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        # do_show
            if args[0] not in {"BaseModel", "User"}:
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

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
        elif args[0] not in {"BaseModel", "User"}:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])

            if not os.path.exists(self.__file_path):
                print("Error: 'file.json' not found.")
                return

            all_objects = self.__objects
            instance = all_objects.get(key)
            if instance is None:
                print("** no instance found **")
            else:
                del all_objects[key]
                self.save()

    def do_all(self, args):
        """Prints all string representations of instances based on the class name"""
        all_objects = storage.all()

        if not args or args[0] not in {"BaseModel", "User"}:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in all_objects.items() if args[0] in key])


    def do_update(self, args):
        if args[0] not in {"BaseModel", "User"}:
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
            # Your code for updating the instance goes here

                setattr(instance, args[2], args[3])
                instance.save()
if __name__ == '__main__':
    HBNBCommand().cmdloop()
