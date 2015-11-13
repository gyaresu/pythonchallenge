import urllib
import re

print "Starting search"

# Ran this first and then it choked. (Clue says 400 times is enough)
#num = 12345

# Ran this second and then it choked
#num = 94485

# Ran this third and error below happened
#and the next nothing is 16044
#Yes. Divide by two and keep going.

# and the next nothing is 82682
# There maybe misleading numbers in the
# text. One example is 82683. Look only for the next nothing and the next nothing is 63579

# and the next nothing is 66831
# peak.html

num = 63579

def fetch(u):
    page = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % u).read()
    n = re.match("and the next nothing is ([0-9]+)", page)
    print page
    return n.group(1)

for i in range(0, 400):
    num = fetch(num)
