import math
import skimage.graph
import numpy as np
from itertools import permutations
from copy import deepcopy

# the graph uses [x,y] notation, so loop through y for x
def buildGraph():
    graph = []
    for x in range(0, lenx):
        graphline = []
        for y in range(0, leny):
            if grid[y][x] != '#':
                graphline.append(1)
            else:
                graphline.append(9999999)
        graph.append(graphline)
    return(graph)

# grid[y][x]
grid = {}
# points[d] = (x, y)
spoint = None
points = {}

lenx = 0
leny = 0

y = 0
with open("input24.txt") as fp:
    for line in fp:
        grid[y] = {}
        line = line.strip()
        for x in range(0,len(line)):
            subchr = line[x]
            grid[y][x] = subchr
            if subchr != "#" and subchr != ".":
                if subchr == "0":
                    spoint = (x, y)
                else:
                    points[subchr] = (x, y)
        y += 1

lenx = len(grid[0])
leny = len(grid)

perms = list(permutations(points, len(points)))
graph = np.array(buildGraph())

shortestp = 999999
for p in perms:
    psum = 0
    apoint = spoint
    for e in range(0, len(p)):
        npoint = points[p[e]]
        
        path, cost = skimage.graph.route_through_array(graph, [apoint[0],apoint[1]], [npoint[0], npoint[1]], fully_connected=False, geometric=False)
        if cost > 9999990:
            #print(path)
            print("no path found")
        else:
            # visual debug stuff
            #print(graph)
            #print(path)
            #pgrid = deepcopy(grid)
            #for z in path:
            #    pgrid[z[1]][z[0]] = '='

            #for t in pgrid:
            #    line = str(t)
            #    for u in pgrid[t]:
            #        line += pgrid[t][u]
            #    print(line)

            #print("Steps =",len(path)-1)
            psum += len(path)-1

        apoint = npoint
    
    # UNCOMMENT FOR PART B
    #path, cost = skimage.graph.route_through_array(graph, [apoint[0],apoint[1]], [spoint[0], spoint[1]], fully_connected=False, geometric=False)
    #if cost > 9999990:
    #    #print(path)
    #    print("no path found")
    #else:
    #    psum += len(path)-1

    if psum < shortestp:
        shortestp = psum
    
print("Shortest path: ", shortestp)


