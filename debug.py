#!/usr/bin/env python

import os
os.system('echo "Mapper input:"')
os.system('cat data.txt | tee /dev/tty | python mapper.py | tee /dev/tty | python reducer.py')
