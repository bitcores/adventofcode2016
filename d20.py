from copy import deepcopy

minip = 0
#maxip = 9
maxip = 4294967295
rules = []
with open("input20.txt") as fp:
    for line in fp:
        line = line.strip()
        rules.append(line)

change = True
while change:
    change = False
    for x in rules:
        nums = x.split('-')
        if int(nums[0]) <= minip and int(nums[1]) > minip:
            minip = int(nums[1])+1
            change = True

#part 1
print(minip)

#part 2
newrules = []
# filter out ranges contained within other rules
for e in rules:
    contained = False
    nums = e.split('-')
    for r in rules:
        if e == r:
            continue
        gnums = r.split('-')
        if int(nums[0]) >= int(gnums[0]) and int(nums[1]) <= int(gnums[1]):
            contained = True
    if contained == False:
        newrules.append(e)

rules = deepcopy(newrules)

# merge ranges that overlap
def findOverlap(g):
    gnums = g.split('-')
    for r in rules:
        if g == r:
            continue
        rnums = r.split('-')
        if int(gnums[0]) < int(rnums[0]) and int(gnums[1]) > int(rnums[0]) and int(gnums[1]) < int(rnums[1]):
            return findOverlap(r)
    return(gnums[1])

newrules = []
for e in rules:
    overlap = False
    contained = False
    enums = e.split('-')
    for r in rules:
        if e == r:
            continue
        rnums = r.split('-')
        if int(enums[0]) < int(rnums[0]) and int(enums[1]) > int(rnums[0]) and int(enums[1]) < int(rnums[1]):
            h = findOverlap(r)
            for g in newrules:
                if r == g:
                    continue
                gnums = g.split('-')
                if int(enums[0]) >= int(gnums[0]) and int(h) <= int(gnums[1]):
                    contained = True
            if contained == False:
                newrules.append(enums[0]+"-"+h)
          
            overlap = True
    if overlap == False:
        newrules.append(e)

print(len(newrules))
rules = deepcopy(newrules)
newrules = []
# filter out ranges contained within other rules
for e in rules:
    contained = False
    nums = e.split('-')
    for r in rules:
        if e == r:
            continue
        gnums = r.split('-')
        if int(nums[0]) >= int(gnums[0]) and int(nums[1]) <= int(gnums[1]):
            contained = True
    if contained == False:
        newrules.append(e)

print(len(newrules))

# now i can just deduct the length of the ranges from the max number of ips
#total ips = maxip+1
validipcnt = maxip+1
for o in newrules:
    onums = o.split('-')
    validipcnt = validipcnt - (int(onums[1]) - int(onums[0]) + 1)

print(validipcnt)