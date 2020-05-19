from copy import deepcopy
from math import floor

#elvno = 8
elvno = 3012210

elves = []
for e in range(1, elvno+1):
    elves.append(e)
elves2 = deepcopy(elves)

## part 1
pos = 0
while len(elves) > 1:
    nelves = []
    for p in range(pos,len(elves), 2):
        nelves.append(elves[p])
    if len(elves) % 2 != 0:
        if pos == 0:
            pos = 1
        else:
            pos = 0
    elves = deepcopy(nelves)

print("Part 1: ", elves)

## part 2
pos = 0
gtype = 0
nelves = deepcopy(elves2)
half = floor(len(nelves) / 2)
r1 = nelves[:half]
r2 = nelves[half:]
switch = True
cnt = 0
if len(r1) != len(r2):
    cnt = 1

while True:
    #print(r1)
    #print(r2)
    #print(pos)
    #print(cnt)
    #input()

    if switch:
        if pos > len(r2)-1:
            switch = not switch
            pos = pos - len(r2)
            continue
        r2.pop(pos)
    else:
        if pos > len(r1)-1:
            switch = not switch
            pos = pos - len(r1)
            continue
        r1.pop(pos)        
    
    cnt += 1
    if cnt == 2:
        cnt = 0
        pos += 1

    if (len(r1) == 0 and len(r2) == 1) or (len(r1) == 1 and len(r2) == 0):
        break
    
print("Part 2:")
print(r1, r2)