#!/usr/bin/env python

import sys

# opening file with open

if len( sys.argv ) > 1:
    f = open( sys.argv[1] )
    first_line = f.readline()
else:
    first_line = sys.stdin.readline()

print first_line
