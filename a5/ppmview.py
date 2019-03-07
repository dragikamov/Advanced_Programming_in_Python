# 350112
# a5 1.py
# Dragi Kamov
# d.kamov@jacobs-university.de

from graphics import *
import locale
import sys

#locale.setlocale(locale.LC_ALL, "C")

debug = 1

def read_P3(filename):
	# we need to read in ascii mode
    try:
        f = open(filename, "r")
    except:
        print("Cannot open", filename)
        return

    try:
       file = f.read()
       # split lines by newlines
       lines = file.split(chr(10))
       magic = lines.pop(0)
       val = lines.pop(0).split()
       width = int(val.pop(0))
       if (len(val)):
          height = int(val.pop(0))
       else:
          height = int(lines.pop(0))
       maxnum = lines.pop(0);
    except:
       print("Invalid format!")
       return

    if debug:
        print(width)
        print(height)
        print(maxnum)

    img = Image(Point(width // 2, height // 2), width, height)

    row = 0
    col = 0
    for line in lines:
        # put all the pixel in list
        pix = list(line.split())
        for c in range(0, len(pix), 3):
            col = (col + 1) % width
            if (col == 0):
                row += 1
            red = int(pix[c])
            green = int(pix[c+1])
            blue = int(pix[c+2])

            img.setPixel(col, row, "#%02x%02x%02x" % (red, green, blue))
    f.close()
    return img

def main():
    if len(sys.argv) != 2:
        filename = "ascteapot.ppm"
    else:
        filename = sys.argv[1]
    try:
        f = open(filename, "rb")
    except:
        print("Cannot open file", filename)
        return

    magic = f.read(2)
	# we need to close binary mode
	# either P3 or image handler take care of this now
    f.close()
    if magic == b'P3':
        img = read_P3(filename)
        title = "ASCII PPM Image"

    elif magic == b'P6':
        img = Image(Point(1,1), filename)
		# centered coordinates, we need to adjust
        img.move(img.getWidth() // 2, img.getHeight() // 2)
        title = "Binary PPM Image"
    else:
        print("Wrong magic string:", magic)
        return


    width = img.getWidth()
    height = img.getHeight()
    win = GraphWin(title, width, height)

    img.draw(win)

    print("Done!")
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()
