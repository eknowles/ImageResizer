import os
from PIL import Image

path = "D:\CLIENTS\Random House/1536\Images"


def Resize(theimage):
    basewidth = 650
    baseheight = 450
    datfile = os.path.join(path, theimage)
    img = Image.open(datfile)
    width, height = img.size
    if width > height:
        landscape = True
    else:
        landscape = False
    if landscape and width > basewidth:
        wpercent = (basewidth / float(width))
        hsize = int((float(height) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        print "Sizing landscape image " + theimage + " to width of " + str(basewidth)
        img.save(datfile)
    if not landscape and height > baseheight:
        hpercent = (baseheight / float(height))
        wsize = int((float(width) * float(hpercent)))
        img = img.resize((wsize, baseheight), Image.ANTIALIAS)
        print "Sizing portrait image " + theimage + " to height of " + str(baseheight)
        img.save(datfile)


listing = os.listdir(path)
for infile in listing:
    Resize(infile)
