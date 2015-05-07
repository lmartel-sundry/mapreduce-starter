#!/usr/bin/env python

from __future__ import print_function
import sys
import random
from collections import defaultdict

### CHANGE ONLY THIS FUNCTION
# Input:
# `key` : String or Tuple[String].              One key output by the mappers. 
# `values` : List[String] or List[List[String]. List of all values output by mappers for that key
#
# Example:
# Mapper 1 outputs 'A -> B C'
# Mapper 2 outputs 'B C -> C D E F'
# Mapper 3 outputs 'A -> C D'
# then...
# Reducer 1 input: 'A', [['B', 'C'], ['C', 'D']]
# Reducer 2 input: ('B', 'C'), [['C', 'D', 'E', 'F']]
def reducer(key, values):

    friend_sets = [set(l) for l in values]
    mutual_friends = set.intersection(*friend_sets)
    output(key[0], key[1], sorted(mutual_friends))


def output(person_a, person_b, mutual_friends):
    print('%s, %s -> %s' % (person_a, person_b, mutual_friends and ' '.join(mutual_friends)))


if __name__ == "__main__":
    print('Reducer step starting.', file=sys.stderr)
    values_by_key = defaultdict(list)

    # Parse input
    for line in sys.stdin:
        key, value = line.strip().split(' -> ')
        key_tokens = key.split()
        value_tokens = value.split()
        if len(key_tokens) > 1:
            key = tuple(key_tokens)

        if len(value_tokens) > 1:
            value = value_tokens

        values_by_key[key].append(value)

    # Simulate shuffle step
    reducer_inputs = []
    for key in sorted(values_by_key):
        values = values_by_key[key]
        random.shuffle(values)
        reducer_inputs.append((key, values))

    # Do reduce step
    for key, values in reducer_inputs:
        reducer(key, values)
