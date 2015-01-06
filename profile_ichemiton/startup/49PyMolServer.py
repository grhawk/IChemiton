## Run the pymol server
from __future__ import print_function

print('\nStarting PyMol as server... ')
import subprocess as sp
import os
FNULL = open(os.devnull, 'w')
sp.Popen(['pymol', '-R'], stdout=FNULL, stderr=sp.STDOUT)
print('...Done')
