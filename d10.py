
tree = {}
bots = {}
botset = set()

with open("input10.txt") as fp:
    for line in fp:
        line = line.strip()
        lp = line.split(" ")
        if lp[2] == "gives":
            lo = "o"
            if lp[5] == "bot":
                lo = "b"
            hi = "o"
            if lp[10] == "bot":
                hi = "b"
            tree["b"+lp[1]] = (lo+lp[6],hi+lp[11])
            botset.add("b"+lp[1])
        else:
            if not "b"+lp[5] in bots:
                bots["b"+lp[5]] = set()
            bots["b"+lp[5]].add(int(lp[1]))

print(tree)
print(bots)
print(botset)

def stepbots(nxtp):
    li = []
    for x in bots[nxtp]:
        li.append(x)
    if li[0] > li[1]:
        if tree[nxtp][0][0] == "o" or len(bots[tree[nxtp][0]]) < 2:
            bots[tree[nxtp][0]].add(li[1])
        if tree[nxtp][1][0] == "o" or len(bots[tree[nxtp][1]]) < 2:
            bots[tree[nxtp][1]].add(li[0])
    else:
        if tree[nxtp][0][0] == "o" or len(bots[tree[nxtp][0]]) < 2:
            bots[tree[nxtp][0]].add(li[0])
        if tree[nxtp][1][0] == "o" or len(bots[tree[nxtp][1]]) < 2:
            bots[tree[nxtp][1]].add(li[1])

for y in range(0,100):
    for x in botset:
        if x in bots and len(bots[x]) == 2:
            if not tree[x][0] in bots:
                bots[tree[x][0]] = set()
            if not tree[x][1] in bots:
                bots[tree[x][1]] = set()
            
            stepbots(x)

            if 17 in bots[x] and 61 in bots[x]:
                print(x)
                

#print(bots)
for z in bots:
    if z[0] == "o":
        print(z, bots[z])