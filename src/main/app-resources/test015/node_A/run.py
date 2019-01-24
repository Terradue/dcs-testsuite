#!/opt/anaconda/envs/python35/bin/python

import sys
import os
import subprocess
from shutil import copyfile

import cioppy
ciop = cioppy.Cioppy()

for input in sys.stdin:
    
    filename = os.path.join(ciop.tmp_dir,input.strip())
    f = open(filename,"w")
    f.write("Empty\n")
    f.close()
 
    copyfile(filename, filename + '.bkp')
 
    ciop.log('INFO', 'input: ' + input)
    ciop.log('INFO', 'filename:' + filename)
    ciop.log('INFO', 'parameter: ' + ciop.getparam("param1"))

    # ciop.publish tests
    ## nominal mode
    ciop.publish(filename)
    ## metalink
    ciop.publish(filename, metalink=True)
    ## mode=silent
    ciop.publish(input, mode='silent')
    ## mode=anonymous
    ciop.publish(filename + '.bkp', mode='anonymous')
