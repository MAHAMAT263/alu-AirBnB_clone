#!/usr/bin/python3
""" the console part """
import cmd

class HBNBCommand(cmd.Cmd):
     """
    This is the HBNBCommand class for the command interpreter.
    It inherits from cmd.Cmd and provides specific commands.
    """
    
    prompt = "(hbnb)"

    def do_quit (self, arg):
        """Quit command to exit the program"""
        return True
    def do_EOF (self, arg):
        """EOF to quit the program at the end of the file"""
        print("")
        return True
    def help_quit(self):
        """Help message for the quit command"""
        print("Quits the program")

    def help_EOF(self):
        """Help message for the EOF command"""
        print("Exits the program when End of File is reached")

    def emptyline(self):
        """Do nothing on empty line + ENTER"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
