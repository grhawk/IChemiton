from __future__ import print_function

import IPython.utils as ut
import sys, os

IChemiton_dir = ut.path.locate_profile('ichemiton')

sys.path.append(os.path.join(IChemiton_dir, 'modules'))

print('\nChemistry Modules:\n cinfony\n cinfony -> rdk, pybel\n PyMol')
from cinfony import rdk, pybel  #https://code.google.com/p/cinfony/
import PyMol
import cinfony

print('\nMath Modules:\n numpy as np\n mathplotlib.pyplot as plt\n pandas as pd')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
# Settings for pandas
pd.set_option('display.notebook_repr_html', True) # Print the data directly in a nice table
pd.set_option('display.max_rows', 500) # Display until to 500 rows


# Set the path for the matplotlib config file
os.environ['MPLCONFIGDIR'] = os.path.join(IChemiton_dir, 'config')

# At a certain point think to use plotly:
# http://nbviewer.ipython.org/gist/nipunreddevil/7734529
