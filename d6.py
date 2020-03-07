
rowlist = []
rowsets = []

with open("input6.txt") as fp:
    for line in fp:
        line = line.strip()
        for x in range(0,len(line)):
            if len(rowlist) < x+1:
                rowlist.append([])
            rowlist[x].append(line[x])
            if len(rowsets) < x+1:
                rowsets.append(set())
            rowsets[x].add(line[x])

#print(rowlist)
#print(rowsets)
outword = ""
for x in range(len(rowsets)):
    lm = 99999
    lchar = ""
    for y in rowsets[x]:
        c = rowlist[x].count(y)
        if c < lm:
            lm = c
            lchar = y
    outword += lchar

print(outword)