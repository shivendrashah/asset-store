import os

import sys

import PIL

from PIL import Image


def compressMe(filepath, verbose=False):

    picture = Image.open(filepath)

    myHeight, myWidth = picture.size

    getSize = os.path.getsize(filepath)

    print("sourceSize", getSize, "bytes", picture.size,  end="\n")

    if (myWidth // 2 > 84 and myHeight // 2 > 84):
        picture = picture.resize(
            (myHeight // 2, myWidth // 2), PIL.Image.ANTIALIAS)

        destFileName = filepath.split(".")[0]+".png"

        picture.save((destFileName),

                     "png",

                     optimize=True,

                     quality=10)

        newSize = os.path.getsize(destFileName)
        print(newSize, myWidth, myHeight)
        while (newSize > 2048 and myWidth // 2 > 84 and myHeight // 2 > 84):
            picture = Image.open(destFileName)
            myHeight, myWidth = picture.size
            picture = picture.resize(
                (myHeight // 2, myWidth // 2), Image.ANTIALIAS)
            picture.save((destFileName),
                         "png",
                         optimize=True,
                         quality=10)
            newSize = os.path.getsize(destFileName)
        print("destSize", newSize, " bytes", picture.size, end="\n")

    return


file = sys.argv[1]
if('.9.png' not in file):
    compressMe(file, True)
    print("Done")
else:
    print("Not allowed to resize")
