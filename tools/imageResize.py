import os, sys
from PIL import Image

size = 600, 600


def image_scale(file):
    a,b = os.path.splitext(file)
    if b in [".jpeg", ".jpg", ".png"]:
        outfile = a + "_standard" + b
        try:
            im = Image.open(file)
            im.thumbnail(size)
            im.save(outfile, im.format)
        except IOError:
            print "cannot create thumbnail for '%s'" % file


def test(root_dir):
    list_dirs = os.walk(root_dir)
    for root, dirs, files in list_dirs:
        for f in files:
            image_scale(os.path.join(root, f))


def main():
    length = len(sys.argv)
    if length <= 1:
        print "need root directory parameter"
        exit()
    elif length > 2:
        print "only one root directory parameter needed"
        exit()
    else:
        argv = sys.argv[1]
        test(argv)

if __name__ == '__main__':
    main()
