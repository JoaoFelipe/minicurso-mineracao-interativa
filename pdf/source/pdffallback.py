from pprint import pformat
from IPython.display import Image, SVG, display

def show(obj, convert=False, count=5):
    if convert or not isinstance(obj, (list, str)):
        obj = pformat(obj).split("\n")
    if isinstance(obj, str):
        obj = obj.split("\n")
    extra = ""    
    if len(obj) > count:
        extra = "\n..."
    print("\n".join(obj[:count]) + extra)

def image(name, width=None):
    if name.endswith(".svg"):
        display(SVG(name))
    else:
        im = Image(name)
        if width is not None:
            im.width = width
        display(im)
