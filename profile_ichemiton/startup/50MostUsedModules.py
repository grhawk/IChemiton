from __future__ import print_function

import IPython.utils as ut
import sys, os

IChemiton_dir = ut.path.locate_profile('ichemiton')

sys.path.append(os.path.join(IChemiton_dir, 'modules'))

print('\nChemistry Modules:\n cinfony\n cinfony -> rdk, pybel\n PyMol')
from cinfony import rdk, pybel  #https://code.google.com/p/cinfony/
import PyMol
import cinfony

print('\nMath Modules:\n numpy as np\n mathplotlib.pyplot as plt')
import numpy as np
import mathplotlib as plt

# Set the path for the matplotlib config file
os.environ['MPLCONFIGDIR'] = os.path.join(IChemiton_dir, 'config')
