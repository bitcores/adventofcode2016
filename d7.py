import re

tlsupported = set()
tlunsupported = []
sslsupported = set()
sslunsupported = []

with open("input7.txt") as fp:
    for line in fp:
        line = line.strip()
        unsupported = False
        sslsup = False
        sslch = ""
        
        subbs = re.findall(r'(\[[^]]*])+', line)
        xb = line
        for bb in subbs:
            xb = xb.replace(bb, "_")
        for ib in subbs:   
            subre = re.findall(r'(\w)\1+', ib)
            dc = -1
            for x in subre:
                dc = ib.find(x+x, dc+1)
                if dc > 0 and len(ib) > dc+2:
                    if ib[dc-1] == ib[dc+2]:
                        #print("u",ib[dc-1:dc+3])
                        tlunsupported.append(line)
                        unsupported = True
            pos = 0
            for y in range(2,len(ib)-2):
                if ib[y-1] == ib[y+1] and ib[y-1] != ib[y]:
                    #print("ssl",ib[y-1:y+2])
                    sslch = ib[y]+ib[y-1]+ib[y]
                    dss = xb.find(sslch)
                    if dss >= 0:
                        sslsupported.add(line)
                    else:
                        sslunsupported.append(line)
            
        if not unsupported:
            scubre = re.findall(r'(\w)\1+', xb)
            dc = -1
            for x in scubre:
                dc = xb.find(x+x, dc+1)
                if dc > 0 and len(xb) > dc+2:
                    if xb[dc-1] == xb[dc+2]:
                        #print("s",xb[dc-1:dc+3])
                        #print(line)
                        #input()
                        tlsupported.add(line)
           
#print(tlsupported)
print(len(tlsupported))
print(len(sslsupported))