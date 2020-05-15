
used = {}
avail = {}
pairs = {}

#datagrid[x][y] = (used, available)
datagrid = {}
sizegrid = {}
emptynode = None
maxx = 0
maxy = 0
maxsize = 0
maxsy = 0

with open("input22.txt") as fp:
    for line in fp:
        line = line.strip()
        if line.find("grid/node") > 0:
            nodes = line[:22].strip()
            nodeu = line[30:36].strip()
            nodea = line[37:43].strip()
            ns = nodes.split("-")
            nname = ns[1]+ns[2]
            used[nname] = int(nodeu[:-1])
            avail[nname] = int(nodea[:-1])
            #print(nname, nodeu[:-1], nodea[:-1])

            # part 2 data
            nodesize = line[23:29].strip()
            if int(nodesize[:-1]) > maxsize:
                maxsize = int(nodesize[:-1])
                maxsy = int(ns[2][1:])
            if not int(ns[1][1:]) in datagrid:
                datagrid[int(ns[1][1:])] = {}
                sizegrid[int(ns[1][1:])] = {}
            datagrid[int(ns[1][1:])][int(ns[2][1:])] = (int(nodeu[:-1]), int(nodea[:-1]))
            sizegrid[int(ns[1][1:])][int(ns[2][1:])] = int(nodesize[:-1])
            if int(nodeu[:-1]) == 0:
                emptynode = (int(ns[1][1:]), int(ns[2][1:]))
            if int(ns[1][1:]) > maxx:
                maxx = int(ns[1][1:])
            if int(ns[2][1:]) > maxy:
                maxy = int(ns[2][1:])
            

# part 1
viablepairs = 0
for e in used:
    if used[e] != 0:
        pairs[e] = []
        for x in avail:
            if x != e:
                if used[e] < avail[x]:
                    pairs[e].append(x)
        viablepairs += len(pairs[e])
print("Viable pairs: ", viablepairs)


# part 2
# the datapoint/node we want
datap = (maxx, 0)
steps = 0
# emptynode is our starting point
# what i noticed is that in the data structure there is a barrier of very high
# storage drives "horizontally" blocking direct paths to the desired node
# maxsy holds the y value of this blocking row. we must find the x value of the
# "gap" in the row, which will be the smallest value
minsy = 99999
minsx = -1
for x in range(0,maxx+1):
    if sizegrid[x][maxsy] < minsy:
        minsy = sizegrid[x][maxsy]
        minsx = x

# now that we know where the gap is, calculating the minimum number of moves is
# actually quite simple. first we need to move the empty node adjacent to the desired node
# move the empty node to the gap x value
steps += abs(minsx - emptynode[0])
# move the empty node to the top y value 0
steps += abs(0 - emptynode[1])
# move the empty node adjacent to the desired node
steps += abs(maxx-1 + minsx)
# move the data node into the new empty node
steps += 1
# now, to move the desired data one node left takes 5 steps each time
# so to move from maxx-1 to 0 will be (maxx-1) * 5
steps += (maxx-1) * 5

print("Steps to move: ", steps)

