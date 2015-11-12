import string
import re

biglist = open('./equality.txt').read().split('\n')
joined = string.join(biglist)
clean = joined.replace(' ', '')
result = ''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', clean))
print result
