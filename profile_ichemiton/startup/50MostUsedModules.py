from __future__ import print_function

import IPython.utils as ut
import sys, os

sys.path.append(os.path.join(ut.path.locate_profile('ichemiton'), 'modules'))

print('\nModules:\n cinfony\n cinfony -> rdk, pybel\n PyMol')
from cinfony import rdk, pybel  #https://code.google.com/p/cinfony/
import PyMol
import cinfony
