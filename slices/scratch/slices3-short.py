from rdflib import Graph
from collections import defaultdict

g = Graph()
g.parse('extrescal.ttl',format='ttl')

#grab all of the predicates
predicateList = []
for s, p, o in g:
     predicateList.append(p)

# grab all of the subjects
subjectList = []
for s, p, o in g:
   subjectList.append(s)

#grab all of the objects
objectList = []
for s, p, o in g:
   objectList.append(o)

subObjList = subjectList+objectList

# unique subject/object dictionary
o = {}

i=0
for letter in subObjList:
   letter = letter.decode('UTF-8')
   if ( letter not in o.values() ):
      # i = i + 1
      #letter = letter.decode('UTF-8')
      o[i] = letter
      i = i + 1
   
# unique predicate dictionary

print 'python values'
print 'apple' in o.values()
print '=========end of python values=================='

d = {}

i=0
for letter in predicateList:
      letter = letter.decode('UTF-8')
      if ( letter not in d.values() ):
         # i = i + 1
         #letter = letter.decode('UTF-8')
         d[i] = letter
         i = i + 1

print 'subject object list'
print subObjList
print '================================'
print 'predicate list'
print predicateList
print '================================'

print 'subject object dictionary'
print o
print '================================'

print 'predicate dictionary'
print d
print '================================'

print 'the number of slices: '
print len(d)

# okay, this value has multiple values
fruit = 'http://dbpedia.org/resource/Tristania'

for k, v in o.items():
     if fruit == v:
        print 'the idex of '+ fruit +' is :'
        print k

print '=================break==============='

rows = defaultdict(list)
cols = defaultdict(list)

for subject, predicate, obj in g:
    print '========================================'
    k1 = 0 
    k2 = 0
    k3 = 0
    subject = subject.decode('UTF-8')
    for k, v in o.items():
     if subject == v:
        print 'the index of subject '+ subject
        k1 = k
        print k
    predicate = predicate.decode('UTF-8') 
    for k, v in d.items():
     if predicate == v:
        print 'the idex of '+ predicate 
        k2 = k
        print k
    obj = obj.decode('UTF-8')
    for k, v in o.items():
      if obj == v:
         print 'the index of obj '+obj
         k3 = k
         print k
    print '========================================='
    print '=======print k1=========================='
    print k1 
    print '=======print k2==================='
    print k2
    print '=======print k3============================='
    print k3
    print '==================================='
    rows[k2].append(k1)
    cols[k2].append(k3)

print 'rows: ',rows
print 'cols: ',cols

print rows[0]
