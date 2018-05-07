thelist = [[0,0,0],[1,1,5],[1,2,3]]
print thelist
print thelist[0]
print thelist[0][1]
sublist = [2,2,1]
thelist.append(sublist)
print thelist
i = 0
print thelist[i][0]
print len(thelist)

row = {}
col = {}
for uk in thelist:
    print 'the predicate slice ', uk[1]
    print 'the row #', uk[0]
    print 'the col #', uk[2] 
    row[uk[1]] = uk[0]
    col[uk[1]] = uk[2]

print row
print col
