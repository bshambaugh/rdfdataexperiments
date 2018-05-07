from rdflib import Graph

fr = open('extrescal.ttl','r')
text = fr.read()
fr.close()

print text

g = Graph()
g.parse('extrescal.ttl',format='ttl')
print(len(g))


qres = g.query(
	    """SELECT ?s ?p ?o
       WHERE {
          ?s ?p ?o .
       } """)

test = set()

print('====================================')
print('the test set')
print('====================================')
for row in qres:
    test.add(row)
    print("%s %s %s" % row)

print ('=============break here=============')
for s, p, o in g:
    print s, p, o

