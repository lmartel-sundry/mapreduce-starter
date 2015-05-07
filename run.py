#!/usr/bin/env python

import os
os.system('cat data.txt | python mapper.py | python reducer.py')
