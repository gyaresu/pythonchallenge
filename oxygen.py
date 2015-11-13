from PIL import Image
import re
import urllib
import StringIO

im = Image.open(StringIO.StringIO(urllib.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png').read()))
w,h = im.size

print "Command: print ''.join([chr(im.getpixel((i, h//2))[0]) for i in range(0,w,7)])"
print ''.join([chr(im.getpixel((i, h//2))[0]) for i in range(0,w,7)])
print
print "Command: print ''.join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))"
print ''.join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))
