# https://docs.python.org/2/library/fnmatch.html
import fnmatch
import os

inputDir = ''
inputFile = ''

for file in os.listdir('./%s' % inputDir):
   if fnmatch.fnmatch(file, '*.txt'):
       print file
