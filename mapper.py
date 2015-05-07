#!/usr/bin/env python

import sys

### CHANGE ONLY THIS FUNCTION
# Example input:
# person = 'Alice'
# friends = ['Bob', 'Steve', 'Cindy']
def mapper(person, friends):

    # TODO

    output(None, None)


def output(key, value):
    if type(key) is list or type(key) is tuple:
        key = ' '.join(key)

    if type(value) is list or type(value) is tuple:
        value = ' '.join(value)
        
    print '%s -> %s' % (key, value)


if __name__ == "__main__":
    for line in sys.stdin:
        # Parse input
        person, friends = line.strip().split(' -> ')

        # Do mapper step
        mapper(person.strip(), friends.split())
