import os
# Pulls filename from a dir, print their relative path and absolut path
def printdir(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        print filename
        print os.path.join(dir, filename)
        print os.path.abspath(os.path.join(dir, filename))
