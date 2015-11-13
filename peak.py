import pickle
import urllib

banner = urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read()
data = pickle.loads(banner)

print '\n'.join([''.join([p[0] * p[1] for p in row]) for row in data])
