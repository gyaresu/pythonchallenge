import zipfile
import StringIO
import urllib
import re

num = 90052
data = zipfile.ZipFile(StringIO.StringIO(urllib.urlopen('http://www.pythonchallenge.com/pc/def/channel.zip').read()))
comments = []

def next(p):
    content = data.read(p)
    n = re.match('Next nothing is ([0-9]+)', content)
    print n.group(1)
    return n.group(1)

for i in range(len(data.namelist())):
    comments.append(num)
    num = next('%s.txt' % num)

print ''.join([data.getinfo('%s.txt' % p).comment for p in comments])
