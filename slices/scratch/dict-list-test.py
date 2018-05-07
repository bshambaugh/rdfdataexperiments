# https://stackoverflow.com/questions/960733/python-creating-a-dictionary-of-lists
from collections import defaultdict
d = defaultdict(list)
a = ['1', '2','3','4']
for i in a:
   for j in range(int(i), int(i) + 2):
      print 'j is:', j 
      d[j].append(i)

print d

f = defaultdict(list)
f[0].append(1)
f[0].append(2)
f[1].append(3)
f[1].append(2)

print f
