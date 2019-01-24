#!/opt/anaconda/envs/python35/bin/python

import sys
import cioppy

ciop = cioppy.Cioppy()

for input in sys.stdin:
    ciop.log('INFO', input)
