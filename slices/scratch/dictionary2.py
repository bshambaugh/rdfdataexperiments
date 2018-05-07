tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print tel

print tel.keys()

print 'guido' in tel

thearray = ['apple','banana','cherry','apple','pear']

thedict = {}

i = 0

for el in thearray:
   if ( el not in thedict.values()):
      i = i + 1
      #  print len(thedict)
      print i
      thedict[i] = el
 #      thedict[el] = i

print thedict

print 'apple' in thedict.values()

fruit = 'pear'

for k, v in thedict.items():
   if fruit == v or isinstance(v, list) and fruit in v:
       print k

for k, v in thedict.items():
   if fruit == v:
       print k

