from copy import deepcopy
keypad = [["X","X",1,"X","X"],["X",2,3,4,"X"],[5,6,7,8,9],["X","A","B","C","X"],["X","X","D","X","X"]]
#start on 5
pos = [2,0]
codes = []
pswd = []

with open("input2.txt") as fp:
    for line in fp:
        line = line.strip()
        codes.append(line)

#pos y,x
#U y -1
#D y +1
#L x -1
#R x +1

def checkbounds(p):
    if p < 0:
        return 0
    if p > 4:
        return 4
    return p

for c in codes:
    for m in c:
        tmp = deepcopy(pos)
        if m == "U":
            pos[0] -= 1
        if m == "D":
            pos[0] += 1
        if m == "L":
            pos[1] -= 1
        if m == "R":
            pos[1] += 1
        pos[0] = checkbounds(pos[0])
        pos[1] = checkbounds(pos[1])
        if keypad[pos[0]][pos[1]] == "X":
            pos = deepcopy(tmp)

    pswd.append(keypad[pos[0]][pos[1]])

print(pswd)

