from __future__ import print_function
from IPython.core.magic import (Magics, magics_class, 
                                line_magic, cell_magic, line_cell_magic)
import os

IChemiton_dir = ut.path.locate_profile('ichemiton')
bindir = os.path.join(IChemiton_dir, 'bin')

@magics_class
class MyMagics(Magics):

    notebook_dir = ''

    @line_magic
    def plot(self, *args):
        """Use the pyplot script to display a graph in the notebook
        Use %plot -h for help"""
        pyplot = os.path.join(bindir, 'pyplot')
        get_ipython().magic('%run '+str(pyplot)+' '+' '.join(args))
        return

    # @line_magic
    # def xyz3D(self, filename):
    #     """Display a 3D molecule from an xyz file using pymol"""
    #     get_ipython().magic('%load_ext display_molecules')
    #     print(self.notebook_dir)
    #     filename = os.path.join(self.notebook_dir, filename)
    #     print(filename)
    #     v = PyMol.MolViewer()
    #     mol = pybel.readfile('xyz', str(filename)).next()
    #     v.ShowMol(mol)
    #     v.GetPNG()
    #     return

ip = get_ipython()
ip.register_magics(MyMagics)
