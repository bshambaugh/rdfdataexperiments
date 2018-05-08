# https://docs.python.org/2/library/fnmatch.html
import fnmatch
import os

for file in os.listdir('.'):
   if fnmatch.fnmatch(file, '*.txt'):
       print file
