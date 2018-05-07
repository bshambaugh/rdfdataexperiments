exDict = {}



exDict.update({'item3': 3})

print exDict

d = {1: 'http://example.org/member-of', 2 : 'http://example.org/genre', 3 : 'http://example.org/cites'}

print d

#k = len(d) + 1

#d.update({k : 'nope'})

#print d 

print 'http://example.org/member-of' in d.values()

print 'http://example.org/member-of' not in d.values()
#    print 'This is most assuredly false'

if ( 'http://example.org/member-of' in d.values() ):
     print 'nooo'


myList = ['http://example.org/member-of','http://example.org/eva']


for letter in myList:
   print 'the letter is: '+letter
   if ( letter in d.values() ):
      print 'ya '+letter
   else:
      print 'noo '+letter  
      k = len(d) + 1
      d.update({k: letter})

print d 
