# Tiny program that turns a regular string into a badass broken-knight string
# eg. of calling : $python3 paloufTalking.py "I'm like your worst nightmare, Opaline - except I'm alive"

import sys
import random

_oldSentence = sys.argv[1]
_newSentence = ''


i = 0
_rand = random.randint (1, 5)
# looping throug the user input
while i < len(_oldSentence):
    if (_rand == 0):
        if (not _newSentence[i-1].islower):    # if the previous char is an upper
            _newSentence += _oldSentence[i]
            _newSentence += _oldSentence[i+1].upper()
        # elif (_oldSentence[i] == ' '):    # if the current character is a space

        else:
            _newSentence += _oldSentence[i].upper()
            _rand = random.randint (1, 5)
    else:
        _newSentence += _oldSentence[i]

    _rand-=1
    i+=1

print(_newSentence)
