
realrooms = []
realnames = []
decoys = []
sectoridsum = 0

def decypher(l,ro):
    #a 97 to z 122
    ro = ro - (122 - ord(l))
    z = ro % 26
    return chr(96 + z)

with open("input4.txt") as fp:
    for line in fp:

        line = line.strip()
        idsum = line.split("[")
        idsum[1] = idsum[1][:-1]
        parts = idsum[0].split("-")
        rid = parts.pop(-1)
        
        q = 0
        prev = ''
        real = True
        for x in idsum[1]:
            c = idsum[0].count(x)
            if c == 0:
                decoys.append(line)
                real = False
                break
            if q == 0 or c < q:
                q = c
            elif c == q:
                if ord(x) < ord(prev):
                    decoys.append(line)
                    real = False
                    break
            elif c > q:
                decoys.append(line)
                real = False
                break
            prev = x
        if real:
            realrooms.append(line)
            decyname = ""
            for x in parts:
                for y in x:
                    decyname += decypher(y,int(rid))
            realnames.append((decyname,rid))

            sectoridsum += int(rid)
            
#print(realrooms)
#print(decoys)
#print(sectoridsum)
#print(realnames)
for x in realnames:
    if "north" in x[0]:
        print(x)

