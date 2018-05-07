from rdflib import Graph

fr = open('extrescal.ttl','r')
text = fr.read()
fr.close()

print text

g = Graph()
g.parse('extrescal.ttl',format='ttl')
print(len(g))

myList = []

print ('=============break here=============')
for s, p, o in g:
     print p
     myList.append(p)

print myList

# grab all of the subjects
subjectList = []
for s, p, o in g:
   subjectList.append(s)

#grab all of the objects
objectList = []
for s, p, o in g:
   objectList.append(o)

#construct a list that contains subjects and objects
print 'here is a subject with object list'
print '================================================'
subObjList = subjectList+objectList
print subObjList
print '================================================'

print 'unique subject/object list'
o = {}

for letter in subObjList:
   print 'the letter is: '+letter
   if ( letter not in o.values() ):
      k = len(o) + 1
      o.update({k: letter})
    
print o

print 'get o'
print len(o)
print o[5]

#uniqueList = []
#for letter in myList:
#   if letter not in uniqueList:
#      uniqueList.append(letter)

#print uniqueList

d = {}

for letter in myList:
   print 'the letter is: '+letter
   if ( letter in d.values() ):
      print 'ya '+letter
   else:
      print 'noo '+letter
      k = len(d) + 1
      d.update({k: letter})

print d

print 'the number of slices: '
print len(d)

#uniqueDict = {}
#for letter in myList:
#    print letter
#   if letter not in uniqueDict.values():
#      uniqueDict.update(letter)


#semweb=rdflib.URIRef('http://dbpedia.org/resource/Tristania')
#type=g.value(semweb, rdflib.RDFS.label)

