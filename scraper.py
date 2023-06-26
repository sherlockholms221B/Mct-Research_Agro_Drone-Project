import time as t, argparse as arg
from collections import namedtuple


class Initiator:
    def __int__(self, message):
        self.message = message

    def main(self):
        print(self.message)


initaite = Initiator()
initaite.message = 'this is the initiator class'
initaite.__int__(message=initaite.message)

a = namedtuple('course', 'tech')
