import hashlib
import re

#ki = 'abc'
ki = 'ihaygndm'
found = False
c = 0

thoulist = []
gkeys =[]

# dumb function for hashing an index 2016 times
def stretchHash(shash):
    for r in range(0,2016):
        m = hashlib.md5()
        m.update(shash.encode('utf-8'))
        shash = m.hexdigest()
    return shash

# populate list of 1001 keys
for p in range(0,1001):
    m = hashlib.md5()
    m.update(ki.encode('utf-8'))
    m.update(str(c+p).encode('utf-8'))
    thoulist.append(stretchHash(m.hexdigest()))

while len(gkeys) < 64:
    # check the first key in the list for a triplet
    res = re.search(r'(.)\1{2}', thoulist[0])
    if res != None:
        s = res.group(0)
        #print(s)
        #input()
        # check the next 1000 keys in the list for a (5 set) of the same value
        for x in range(1,1001):
            regx = r'('+s[0]+'){5}'
            chk = re.search(regx, thoulist[x])
            if chk != None:
                #print(thoulist[x])
                #input()
                # save the index (c) and it's hash to the good keys list
                gkeys.append((c,thoulist[0]))
                break

    # pop the first key in the list, generate a new 1001th key
    thoulist.pop(0)
    c += 1
    m = hashlib.md5()
    m.update(ki.encode('utf-8'))
    m.update(str(c+1000).encode('utf-8'))
    thoulist.append(stretchHash(m.hexdigest()))

# print the last (64th) good key
print(gkeys[63])