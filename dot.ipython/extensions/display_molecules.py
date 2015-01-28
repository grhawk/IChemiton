def display_pil_image(im):
    from IPython.core import display
    from io import BytesIO

    b = BytesIO()
    im.save(b, format='png')
    data = b.getvalue()

    ip_img = display.Image(data=data, format='png', embed=True)
    return ip_img._repr_png_()


def load_ipython_extension(ipython):

    print 'Loading display hooks'

    from PIL import Image
    png_formatter = ipython.get_ipython().display_formatter.formatters['image/png']
    dpi = png_formatter.for_type(Image.Image, display_pil_image)



def unload_ipython_extension(ipython):

    print 'Unloading display hooks'

    from PIL import Image
    png_formatter = ipython.get_ipython().display_formatter.formatters['image/png']
    def donothing(im):
        pass

    dpi = png_formatter.for_type(Image.Image, donothing)
