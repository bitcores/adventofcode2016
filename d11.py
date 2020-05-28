from copy import deepcopy
from itertools import combinations
from random import shuffle


floordict = {}
floordict[0] = set()
floordict[1] = set()
floordict[2] = set()
floordict[3] = set()

# testing data
#floordict[0].add("HM")
#floordict[0].add("LM")
#floordict[1].add("HG")
#floordict[2].add("LG")

# real input
#part 1
floordict[0].add("SG")
floordict[0].add("SM")
floordict[0].add("PG")
floordict[0].add("PM")
floordict[1].add("TG")
floordict[1].add("RG")
floordict[1].add("RM")
floordict[1].add("CG")
floordict[1].add("CM")
floordict[2].add("TM")
#part 2
#floordict[0].add("EG")
#floordict[0].add("EM")
#floordict[0].add("DG")
#floordict[0].add("DM")

stepdict = {}
stepdict[0] = []
stepdata = {}
stepdata['ele'] = 0
stepdata['floors'] = floordict
stepdict[0].append(stepdata)
states = []

end = False

def cntmicgen(floorset,ta):
    c = 0
    for x in floorset:
        if x[1] == ta:
            c += 1
    return c

# E can only move if it contains at least one M/G
# E can only move one floor at a time
# if an M ends up on a floor without its paired G, fail
def safeconfig(floorset): 
    # no. unpaired chips
    upc = 0
    # no. generators
    g = 0
    for x in floorset:
        if x[1] == "M" and x[0]+"G" not in floorset:
            upc += 1
        if x[1] == "G":
            g += 1
    # any unpaired chips will be fried by a generator
    if g > 0 and upc > 0:
        return False
    return True

# after getting this solution to work, but extremely slowly, i did look online for other
# solutions and got this hint at a way to improve speed, though it took me some time to get 
# it implemented due to some logic errors on my part of when a state should be saved
# basically, any legal configuration with the same elevator floor and number of generators and 
# chips on each floor is equal. so if you have already reached such a configuration on a 
# previous step, or already on this step, then you can discard extra instances of that
# configuration. this is much faster than just looking for identical configurations
# my logic mistake in implementation was saving illegal states too, which could block some
# legal configurations (depending how the generators and chips are arranged)
def makestate(sdict):
    statestr = ""
    statestr += str(sdict['ele'])
    for x in range(0, 4):
        statestr += str(cntmicgen(sdict['floors'][x], "M"))+str(cntmicgen(sdict['floors'][x], "G"))
    return statestr

gencnt = 0
for f in range(0,4):
    gencnt += cntmicgen(floordict[f],"G")

step = 0
while True:
    if len(stepdict[step]) == 0:
        break
    # check if solution has been found
    for x in stepdict[step]:
        # everything is on the top floor, break out
        if x['ele'] == 3 and cntmicgen(x['floors'][3], "G") == gencnt and cntmicgen(x['floors'][3], "M") == gencnt:
            end = True
            print("Result in: ", step)
            break
    if end:
        break

    stepdict[step+1] = []
    for x in stepdict[step]: 
        ele = x['ele']
        fdict = x['floors']
        
        movelist = []
        for i in fdict[ele]:
            movelist.append([i])
        combos = list(combinations(fdict[ele], 2))
        for c in combos:
            movelist.append(c)

        # remove invalid moves for going up
        if ele < 3:
            for m in movelist:
                newdict = {}
                newdict['ele'] = ele+1
                newdict['floors'] = deepcopy(fdict)
                for e in m:
                    newdict['floors'][ele+1].add(e)
                for r in m:
                    newdict['floors'][ele].remove(r)
                    
                newstate = makestate(newdict)
                if newstate in states:
                    continue
                if safeconfig(newdict['floors'][ele+1]) and safeconfig(newdict['floors'][ele]):
                    # check if the new arrangement matches an old one
                    stepdict[step+1].append(newdict)
                    states.append(newstate)
                        
        # remove invalid moves for going down
        if ele > 0:
            for m in movelist:
                newdict = {}
                newdict['ele'] = ele-1
                newdict['floors'] = deepcopy(fdict)
                for e in m:
                    newdict['floors'][ele-1].add(e)
                for r in m:
                    newdict['floors'][ele].remove(r)  

                newstate = makestate(newdict)
                if newstate in states:
                    continue
                if safeconfig(newdict['floors'][ele-1]) and safeconfig(newdict['floors'][ele]):
                    # check if the new arrangement matches an old one                 
                    stepdict[step+1].append(newdict)
                    states.append(newstate)
                        
    print(step, '-', len(stepdict[step+1]))  
    step+=1


print("Simulation end")