import hashlib
from copy import deepcopy

#ki = 'ulqzkmiv'
ki = 'udskfozm'

dirdict = {0: 'U', 1: 'D', 2: 'L', 3: 'R'}
opdr = ['b','c','d','e','f']

s = [0,0]
g = [3,3]

def testPath(path):
    p = deepcopy(s)
    for v in path:
        if v == 'U':
            p[1] -= 1
        if v == 'D':
            p[1] += 1
        if v == 'L':
            p[0] -= 1
        if v == 'R':
            p[0] += 1
        if p[0] < 0 or p[0] > 3 or p[1] < 0 or p[1] > 3:
            # if the path has gone out of bounds, return 2
            return(2)
    if p == g:
        return(1)
    return(0)


def tryPath(thash):
    global glist
    plist = []
    for x in thash:
        tpath = x[len(ki):]
        #print(tpath)
        tpchk = testPath(tpath)
        if tpchk == 1:
            glist.append(tpath)
        elif tpchk == 0:
            m = hashlib.md5()
            m.update(x.encode('utf-8'))
            shash = m.hexdigest()
            doors = shash[:4]
            for d in range(0,4):
                if doors[d] in opdr:
                    plist.append(x+dirdict[d])
    if len(plist) > 0:
        tryPath(plist)
    return

glist = []
tryPath([ki])
print("Part 1 ",glist[0])
print("Part 2 ",len(glist[-1]))
    