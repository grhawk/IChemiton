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

    @line_magic
    def mplot(self, *args):
        """Use the pyplot script to display a graph in the notebook
        Use %mplot -h for help"""
        mpyplot = os.path.join(bindir, 'mpyplot')
        get_ipython().magic('%run '+str(mpyplot)+' '+' '.join(args))
        return

    @line_magic
    def video(self, *args):
        """Load the video in the file `fname`, with given mimetype, and display as HTML5 video.
        Usage: %video filename, mimetype
        """
        fname, mimetype = args[0].split(', ')
        from IPython.display import HTML
        video_encoded = open(fname, "rb").read().encode("base64")
        video_tag = '<video controls alt="test" src="data:video/{0};base64,{1}">'.format(mimetype, video_encoded)
        return HTML(data=video_tag)

ip = get_ipython()
ip.register_magics(MyMagics)
