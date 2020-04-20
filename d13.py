import math
import skimage.graph
import numpy as np

def checkspace(x,y):
    out = (x*x + 3*x + 2*x*y + y + y*y) + favnum
    bt = "{0:b}".format(out)
    if not bt.count("1") % 2:
        return(".")
    else:
        return("#")

def checkconn(x,y):
    global connections
    if y in grid:
        if x-1 in grid[y] and grid[y][x-1] == '.':
            connections[(x, y)].add((x-1, y))
            connections[(x-1, y)].add((x, y))
        if x+1 in grid[y] and grid[y][x+1] == '.':
            connections[(x, y)].add((x+1, y))
            connections[(x+1, y)].add((x, y))
    if y-1 in grid:
        if x in grid[y-1] and grid[y-1][x] == '.':
            connections[(x, y)].add((x, y-1))
            connections[(x, y-1)].add((x, y))
    if y+1 in grid:
        if x in grid[y+1] and grid[y+1][x] == '.':
            connections[(x, y)].add((x, y+1))
            connections[(x, y+1)].add((x, y))

def buildGraph():
    graph = []
    for z in range(0, mazesize):
        graphline = []
        y = z
        for z1 in range(0, mazesize):
            x = z1
            if grid[x][y] == '.':
                graphline.append(1)
            else:
                graphline.append(9999999)
        graph.append(graphline)
    return(graph)

grid = {}
#connections = {(0,0):[(0,1)]}
connections = {}

#favnum = 10
favnum = 1350
mazesize = 50

for y in range(0,mazesize):
    if y not in grid:
        grid[y] = {}
    for x in range(0,mazesize):
        grid[y][x] = checkspace(x,y)
        if grid[y][x] == ".": 
            connections[(x,y)] = set()
            checkconn(x,y)

# source is 1,1
# target is 31,39
graph = np.array(buildGraph())
path, cost = skimage.graph.route_through_array(graph, [1,1], [31,39], fully_connected=False, geometric=False)
if cost > 9999990:
    print(path)
    print("no path found")
else:
    #print(graph)
    print(path)
    for z in path:
        grid[z[1]][z[0]] = '='

    for t in grid:
        line = str(t)
        for u in grid[t]:
            line += grid[t][u]
        print(line)

    print("Steps =",len(path)-1)

# how many places can you reach within 50 steps (including start point)
# loop 50,50? there are no straight lines so
maxplaces = 0
for u in range(0,mazesize):
    for i in range(0,mazesize):
        path, cost = skimage.graph.route_through_array(graph, [1,1], [i,u], fully_connected=False, geometric=False)
        if cost < 9999990:
            if len(path)-1 <= mazesize:
                maxplaces += 1
        
print(maxplaces)