from rdflib import Graph
import json
fr = open('countries.json','r')
text = fr.read()
fr.close()

data = json.loads(text)

def happyneighbors(somedata):
 result = ''
 prefix = '@prefix base: <http://example.org/> . \n@prefix Country: <http://example.org/Country/> . \n@prefix CountryCode: <http://example.org/countryCode/> . \n'
 for i in range(len(data)):
# grab the first part of the country data
   if (data[i]['region'] == 'Africa'):
      if len(data[i]['borders']) != 0:
        happy = happy = 'Country:'+data[i]['name']['common'].replace(' ','_').replace(',','') + ' base:locatedIn ' + '"'+data[i]['region'].replace(' ','_') + '" ; base:locatedIn ' + '"' + data[i]['subregion'].replace(' ','_') +'" ; base:hasCode ' + 'CountryCode:'+ data[i]['cca3'] + ' ;'
      else:
               happy = happy = 'Country:'+data[i]['name']['common'].replace(' ','_').replace(',','') + ' base:locatedIn ' + '"'+data[i]['region'].replace(' ','_') + '" ; base:locatedIn ' + '"' + data[i]['subregion'].replace(' ','_') +'" ; base:hasCode ' + 'CountryCode:'+data[i]['cca3'] + ' .\n'
# grab some neighbors      
      neighbors = ''
      for k in range(len(data[i]['borders'])):
        if k != len(data[i]['borders']) - 1:
          neighbors = neighbors + ' base:neighborOf ' + 'CountryCode:'+data[i]['borders'][k] + ' ;'
        else:
          neighbors = neighbors + ' base:neighborOf ' + 'CountryCode:'+data[i]['borders'][k] + ' . \n'
#      print(happy+neighbors)
      print(k)
      result = result + happy + neighbors
 return prefix+result


tofile = happyneighbors(data)

fw = open('africa-countries.ttl', 'w')
fw.write(tofile.encode('utf-8'))
fw.close()

print(tofile)

g = Graph()
g.parse('africa-countries.ttl',format='ttl')
print(len(g))

import pprint
for stmt in g:
    pprint.pprint(stmt)

qres = g.query(
    """SELECT DISTINCT ?name2
       WHERE {
          ?name <http://example.org/hasCode> ?code .
          ?name2 <http://example.org/neighborOf> ?code .
          ?name <http://example.org/locatedIn> ?location . 
       } LIMIT 6""")

test = set()

print('====================================')
print('the test set')
print('====================================')
for row in qres:
    test.add(row)
    print("%s" % row)

vres= g.query("""SELECT DISTINCT ?name2
       WHERE {
          ?name <http://example.org/hasCode> ?code .
          ?name2 <http://example.org/neighborOf> ?code .
          ?name <http://example.org/locatedIn> ?location . 
       } LIMIT 12""")

valandtest = set()
# print('the validation + test set')
for row in vres:
    valandtest.add(row)
 #   print("%s" % row)

# print(valandtest)

validation = valandtest - test

print('====================================')
print('validation')
print('====================================')
for n in validation:
    print("%s" % n)

ares = g.query(
    """SELECT DISTINCT ?name
       WHERE {
          ?name <http://example.org/hasCode> ?code .
       }""")

training = set()
# print('the training test set')
for row in ares:
    training.add(row)
#    print("%s" % row)

# print(training)

rtraining = training - valandtest

print('====================================')
print('training')
print('====================================')
for n in rtraining:
    print("%s" % n)
print('====================================')

