#!/usr/bin/python3

import cmd
"""Class HBNBCommand defines the entry point for the cli"""


class HBNBCommand(cmd.Cmd):
    '''This is the entry point'''
    prompt = '(hbnb) '
    file = '~/ALX/AirBnB_clone/models/engine/file_storage.py'
    def do_EOF(self, line):
        '''Quit Command to exit program'''
        return True
    do_quit = do_EOF

    def do_hi(self, person):
        if person:
            print("hi", person)
        else:
            print("hi")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
