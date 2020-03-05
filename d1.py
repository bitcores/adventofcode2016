import copy
f = open("input1.txt", "r")
dinp = f.read()
f.close()

dirlist = dinp.split(",")

pathlist = []
pos = [0,0]
# N = 0
# E = 1
# S = 2
# W = 3
# L = -1
# R = 1
p = 0

tdict = {"L": -1, "R": 1}

def changep(t):
    global p
    p += tdict[t]
    if p == 4:
        p = 0
    if p == -1:
        p = 3

#pass this function the start (l) and end (p) points of a line
#pathlist is a list of start and end point lists (lines)
def findinter(l,p):
    for x in pathlist:
        if l[0] == p[0] and x[0][1] == x[1][1]:
            #line is vertical, looking for horizontal line
            if (x[0][0] < x[1][0] and (l[0] > x[0][0] and l[0] < x[1][0])) or (x[0][0] > x[1][0] and (l[0] < x[0][0] and l[0] > x[1][0])):
                if (l[1] < p[1] and (x[0][1] > l[1] and x[0][1] < p[1])) or (l[1] > p[1] and (x[0][1] < l[1] and x[0][1] > p[1])):
                    return([p[0],x[0][1]])

        elif l[1] == p[1] and x[0][0] == x[1][0]:
            #line is horizonal, looking for vertical line
            if (x[0][1] < x[1][1] and (l[1] > x[0][1] and l[1] < x[1][1])) or (x[0][1] > x[1][1] and (l[1] < x[0][1] and l[1] > x[1][1])):
                if (l[0] < p[0] and (x[0][0] > l[0] and x[0][0] < p[0])) or (l[0] > p[0] and (x[0][0] < l[0] and x[0][0] > p[0])):
                    return([p[1],x[0][0]])
    return 0


for x in dirlist:
    lpos = copy.deepcopy(pos)
    c = x.strip()
    turn = c[0]
    steps = int(c[1:])
    changep(turn)
    if p == 0:
        pos[1] += steps
    if p == 1:
        pos[0] -= steps
    if p == 2:
        pos[1] -= steps
    if p == 3:
        pos[0] += steps
    
    # start check for part 2
    back = findinter(copy.deepcopy(lpos), copy.deepcopy(pos))
    if back != 0:
        print("intercept ", abs(back[0]) + abs(back[1]))
        break
    # end check for part 2
    pathlist.append([copy.deepcopy(lpos),copy.deepcopy(pos)])

#print(pathlist)
#print(pos)
print(abs(pos[0]) + abs(pos[1]))
