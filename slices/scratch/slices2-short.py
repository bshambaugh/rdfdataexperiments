from rdflib import Graph

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

for letter in subObjList:
   if ( letter not in o.values() ):
      k = len(o) + 1
      letter = letter.decode('UTF-8')
      # change this, the k is inconsistent (maybe clean the array first???)
      o.update({letter: k})
   
# unique predicate dictionary

d = {}

for letter in predicateList:
      if ( letter not in d.values() ):
         k = len(d) + 1
         letter = letter.decode('UTF-8')
         #change this, the k is inconsistent (maybe clean the array first??)
         d.update({letter: k})

print 'subject object list'
print subObjList
print '================================'
print 'predicate list'
print predicateList
print '================================'

print 'get o'
print len(o)
value = 'http://dbpedia.org/resource/Vibeke'
print o[u'http://dbpedia.org/resource/Vibeke']
print o[value]
print o

print d

print 'the number of slices: '
print len(d)

