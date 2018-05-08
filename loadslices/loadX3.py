# https://docs.python.org/2/library/fnmatch.html
import fnmatch
import os
from rdflib import Graph
from collections import defaultdict
from scipy.sparse import csr_matrix
from numpy import ones

inputFile = 'extrescal.ttl'

def loadXfromTTL(inputFile):
 g = Graph()
 g.parse(inputFile,format='ttl')

 #grab all of the predicates
 predicateList = []
 for s, p, o in g:
     return s

print loadXfromTTL(inputFile)
