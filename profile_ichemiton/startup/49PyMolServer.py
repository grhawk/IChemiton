## Run the pymol server
from __future__ import print_function
import xmlrpclib

try:
    serv = xmlrpclib.Server('http://%s:%d'%('localhost',9123))
    serv.ping()
except:
    print('\nStarting PyMol as server... ')
    import subprocess as sp
    import os
    import time
    FNULL = open(os.devnull, 'w')
    sp.Popen(['pymol', '-R'], stdout=FNULL, stderr=sp.STDOUT)
    time.sleep(3)
    print('...Done')
else:
    print('\nPymol already running')
