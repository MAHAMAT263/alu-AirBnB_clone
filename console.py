#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    
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
